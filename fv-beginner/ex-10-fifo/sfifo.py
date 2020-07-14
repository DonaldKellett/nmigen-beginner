from nmigen import *
from nmigen.back.pysim import *
from nmigen.asserts import *
from nmigen.test.utils import *
from nmigen.build import *
from nmigen.build import ResourceError
from nmigen.vendor.lattice_ecp5 import *
from nmigen_boards.resources import *
from functools import reduce

import itertools
import os
import subprocess

__all__ = ['SFIFO']

"""
Synchronous FIFO
See http://zipcpu.com/tutorial/lsn-10-fifo.pdf for more details
"""

class SFIFO(Elaboratable):
	def __init__(self, LGFLEN=10, fv_mode=False):
		self.LGFLEN = LGFLEN
		self.i_wr = Signal(1, reset=0)
		self.i_data = Signal(8, reset=0)
		self.o_full = Signal(1, reset=0)
		self.o_fill = Signal(self.LGFLEN + 1, reset=0)
		self.i_rd = Signal(1, reset=0)
		self.o_data = Signal(8, reset=0)
		self.o_empty = Signal(1, reset=1)
		self.fv_mode = fv_mode
	def ports(self):
		return [
			# Write interface
			self.i_wr,
			self.i_data,
			self.o_full,
			self.o_fill,
			# Read interface
			self.i_rd,
			self.o_data,
			self.o_empty
		]
	def elaborate(self, platform):
		m = Module()

		fifo_mem = Memory(width=8, depth=1<<self.LGFLEN, init=[0]*(1<<self.LGFLEN))
		m.submodules.rdport = rdport = fifo_mem.read_port()
		m.submodules.wrport = wrport = fifo_mem.write_port()

		w_wr = Signal(1, reset=0)
		w_rd = Signal(1, reset=0)
		m.d.comb += w_wr.eq(self.i_wr & ~self.o_full)
		m.d.comb += w_rd.eq(self.i_rd & ~self.o_empty)

		wr_addr = Signal(self.LGFLEN + 1, reset=0)
		rd_addr = Signal(self.LGFLEN + 1, reset=0)
		m.d.comb += self.o_fill.eq(wr_addr - rd_addr)
		m.d.comb += self.o_full.eq(self.o_fill == (1 << self.LGFLEN))
		m.d.comb += self.o_data.eq(rdport.data)
		m.d.comb += self.o_empty.eq(self.o_fill == 0)

		m.d.comb += wrport.en.eq(w_wr)
		m.d.comb += wrport.addr.eq(wr_addr)
		m.d.comb += wrport.data.eq(self.i_data)
		with m.If(w_wr):
			m.d.sync += wr_addr.eq(wr_addr + 1)

		m.d.comb += rdport.addr.eq(rd_addr)
		m.d.comb += self.o_data.eq(rdport.data)
		with m.If(w_rd):
			m.d.sync += rd_addr.eq(rd_addr + 1)

		if self.fv_mode:
			"""
			Tie array of past values with fifo_mem for formal verification
			"""
			f_past_fifo_mem = Array(Signal(8, reset=0) for i in range(fifo_mem.depth))
			for i in range(fifo_mem.depth):
				m.d.sync += f_past_fifo_mem[i].eq(fifo_mem[i])

			"""
			Indicator of when Past() is valid
			"""
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			"""
			Assumptions on input pins
			"""
			# i_wr is never de-asserted for more than 10 consecutive clock cycles
			f_past10_valid = Signal(1, reset=0)
			f_past10_ctr = Signal(range(10), reset=0)
			m.d.sync += f_past10_ctr.eq(f_past10_ctr + 1)
			with m.If(f_past10_ctr == 9):
				m.d.sync += f_past10_ctr.eq(f_past10_ctr)
				m.d.sync += f_past10_valid.eq(1)
			with m.If(f_past10_valid & reduce(lambda a, b: a & b, \
				((~Past(self.i_wr, i)) for i in range(1, 11)))):
				m.d.comb += Assume(self.i_wr)
			# i_rd is never de-asserted for more than 10 consecutive clock cycles
			with m.If(f_past10_valid & reduce(lambda a, b: a & b, \
				((~Past(self.i_rd, i)) for i in range(1, 11)))):
				m.d.comb += Assume(self.i_rd)

			"""
			Assumptions on memory
			"""
			# For the read port, given an address in this clock cycle, rdport.data contains the byte
			# under this address in the next clock cycle
			with m.If(f_past_valid):
				m.d.comb += Assume(rdport.data == f_past_fifo_mem[Past(rdport.addr)])
			# For the write port, given an address in this clock cycle, the given data is written to
			# the specified address in memory in the next clock cycle if write enable is asserted, and
			# the memory remains constant otherwise
			with m.If(f_past_valid):
				with m.If(Past(wrport.en)):
					for i in range(fifo_mem.depth):
						m.d.comb += Assume(Mux(i == Past(wrport.addr), \
							fifo_mem[i] == Past(wrport.data), \
							fifo_mem[i] == f_past_fifo_mem[i]))
				with m.Else():
					for i in range(fifo_mem.depth):
						m.d.comb += Assume(fifo_mem[i] == f_past_fifo_mem[i])

			"""
			Properties of o_full
			"""
			# The FIFO is full precisely when all the block RAM is occupied
			m.d.comb += Assert(self.o_full == (self.o_fill == fifo_mem.depth))

			"""
			Properties of o_fill
			"""
			# The size of the FIFO is given by the difference between the write and read addresses with
			# wrapping behavior
			m.d.comb += Assert(self.o_fill == (wr_addr - rd_addr)[:self.LGFLEN+1])
			# The size of the FIFO cannot exceed the capacity of the block RAM
			m.d.comb += Assert(self.o_fill <= fifo_mem.depth)

			"""
			Properties of o_data
			"""
			# o_data should always contain the byte under rd_addr (with the MSB discarded) from the
			# previous clock cycle
			with m.If(f_past_valid):
				m.d.comb += Assert(self.o_data == f_past_fifo_mem[Past(rd_addr)[:self.LGFLEN]])
			# Therefore, when i_rd is asserted and the FIFO is nonempty, o_data should contain the byte
			# under rd_addr (with the MSB discarded) in the next clock cycle
			with m.If(f_past_valid & Past(self.i_rd) & ~Past(self.o_empty)):
				m.d.comb += Assert(self.o_data == f_past_fifo_mem[Past(rd_addr)[:self.LGFLEN]])

			"""
			Properties of o_empty
			"""
			# The FIFO is empty precisely when none of the block RAM is occupied
			m.d.comb += Assert(self.o_empty == (self.o_fill == 0))

			"""
			Properties of w_wr
			"""
			# w_wr should be asserted precisely when i_wr is asserted and the FIFO is not full
			m.d.comb += Assert(w_wr == (self.i_wr & ~self.o_full))

			"""
			Properties of w_rd
			"""
			# w_rd should be asserted precisely when i_rd is asserted and the FIFO is nonempty
			m.d.comb += Assert(w_rd == (self.i_rd & ~self.o_empty))

			"""
			Properties of wr_addr
			"""
			# wr_addr should be initially zero
			with m.If(~f_past_valid):
				m.d.comb += Assert(wr_addr == 0)
			# wr_addr should increment by 1 (with wrapping behavior) if and only if i_wr is asserted
			# and the FIFO is not full
			with m.If(f_past_valid):
				with m.If(Past(self.i_wr) & ~Past(self.o_full)):
					m.d.comb += Assert(wr_addr == (Past(wr_addr) + 1)[:self.LGFLEN+1])
				with m.Else():
					m.d.comb += Assert(Stable(wr_addr))

			"""
			Properties of rd_addr
			"""
			# rd_addr should be initially zero
			with m.If(~f_past_valid):
				m.d.comb += Assert(rd_addr == 0)
			# rd_addr should increment by 1 (with wrapping behavior) if and only if i_rd is asserted
			# and the FIFO is nonempty
			with m.If(f_past_valid):
				with m.If(Past(self.i_rd) & ~Past(self.o_empty)):
					m.d.comb += Assert(rd_addr == (Past(rd_addr) + 1)[:self.LGFLEN+1])
				with m.Else():
					m.d.comb += Assert(Stable(rd_addr))

			"""
			FIFO contract
			Whenever we write two arbitrary values to it in succession, we can always read those same
			values back later
			"""
			# Two arbitrary consecutive addresses
			f_first_addr = AnyConst(self.LGFLEN + 1)
			f_second_addr = AnyConst(self.LGFLEN + 1)
			m.d.comb += Assume(f_second_addr == (f_first_addr + 1)[:self.LGFLEN+1])
			# Two arbitrary data values
			f_first_data = AnyConst(8)
			f_second_data = AnyConst(8)
			# Distance to read address
			f_distance_to_first = Signal(self.LGFLEN + 1, reset=0)
			f_distance_to_second = Signal(self.LGFLEN + 1, reset=0)
			m.d.comb += f_distance_to_first.eq(f_first_addr - rd_addr)
			m.d.comb += f_distance_to_second.eq(f_second_addr - rd_addr)
			# Determine whether f_{first,second}_addr is within the active address of the FIFO
			f_first_addr_in_fifo = Signal(1, reset=0)
			f_second_addr_in_fifo = Signal(1, reset=0)
			with m.If((~self.o_empty) & (f_distance_to_first < self.o_fill)):
				m.d.comb += f_first_addr_in_fifo.eq(1)
			with m.Else():
				m.d.comb += f_first_addr_in_fifo.eq(0)
			with m.If((~self.o_empty) & (f_distance_to_second < self.o_fill)):
				m.d.comb += f_second_addr_in_fifo.eq(1)
			with m.Else():
				m.d.comb += f_second_addr_in_fifo.eq(0)
			# State machine, for formal purposes only
			with m.FSM():
				with m.State('IDLE'):
					m.next = 'IDLE'
					with m.If(w_wr & (wr_addr == f_first_addr) & (self.i_data == f_first_data)):
						m.next = 'WRITE1'
				with m.State('WRITE1'):
					m.next = 'WRITE1'
					m.d.comb += Assert(f_first_addr_in_fifo)
					m.d.comb += Assert(fifo_mem[f_first_addr[:self.LGFLEN]] == f_first_data)
					m.d.comb += Assert(wr_addr == f_second_addr)
					with m.If(w_rd & (rd_addr == f_first_addr)):
						m.next = 'IDLE'
					with m.Elif(w_wr):
						with m.If(self.i_data == f_second_data):
							m.next = 'WRITE2'
						with m.Else():
							m.next = 'IDLE'
				with m.State('WRITE2'):
					m.next = 'WRITE2'
					m.d.comb += Assert(f_first_addr_in_fifo)
					m.d.comb += Assert(fifo_mem[f_first_addr[:self.LGFLEN]] == f_first_data)
					m.d.comb += Assert(f_second_addr_in_fifo)
					m.d.comb += Assert(fifo_mem[f_second_addr[:self.LGFLEN]] == f_second_data)
					with m.If(self.i_rd & (rd_addr == f_first_addr)):
						m.next = 'READ1'
				with m.State('READ1'):
					m.next = 'READ1'
					m.d.comb += Assert(f_second_addr_in_fifo)
					m.d.comb += Assert(fifo_mem[f_second_addr[:self.LGFLEN]] == f_second_data)
					with m.If(self.i_rd):
						m.next = 'IDLE'

		return m

if __name__ == '__main__':
	"""
	Formal Verification
	"""
	class SFIFOTest(FHDLTestCase):
		def test_sfifo(self):
			self.assertFormal(SFIFO(LGFLEN=4, fv_mode=True), mode='prove')
	SFIFOTest().test_sfifo()