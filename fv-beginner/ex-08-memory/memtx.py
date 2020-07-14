from nmigen import *
from nmigen.back.pysim import *
from nmigen.asserts import *
from nmigen.test.utils import *
from nmigen.build import *
from nmigen.build import ResourceError
from nmigen.vendor.lattice_ecp5 import *
from nmigen_boards.resources import *
from functools import reduce
from math import ceil, log

import itertools
import os
import subprocess

from txuart import *

__all__ = ['MemTX', 'MemTXDemo', 'VersaECP5Platform']

"""
Transmitting a long message from block RAM
See http://zipcpu.com/tutorial/lsn-08-memory.pdf for more details
"""

class MemTX(Elaboratable):
	def __init__(self, fv_mode = False):
		self.i_reset = Signal(1, reset=0)
		self.o_busy = Signal(1, reset=1)
		self.o_uart_tx = Signal(1, reset=1)
		self.fv_mode = fv_mode
	def ports(self):
		return [self.i_reset, self.o_busy, self.o_uart_tx]
	def elaborate(self, platform):
		m = Module()

		psalm_bytes = None

		with open('psalm.txt', 'rb') as psalm_file:
			psalm_bytes = list(psalm_file.read())

		if platform is not None and platform != 'formal':
			self.o_uart_tx = platform.request('uart').tx.o
		
		ADDRESS_WIDTH = ceil(log(len(psalm_bytes), 2))
		ram = Memory(width=8, depth=1<<ADDRESS_WIDTH, init=psalm_bytes)
		m.submodules.rdport = rdport = ram.read_port()
		o_addr = Signal(ADDRESS_WIDTH, reset=0)
		i_data = Signal(8)
		m.d.comb += rdport.addr.eq(o_addr)
		m.d.comb += i_data.eq(rdport.data)

		o_wr = Signal(1, reset=0)
		i_busy = Signal(1, reset=0)
		m.submodules.txuart = txuart = TXUART(o_wr, i_data, i_busy, self.o_uart_tx, self.fv_mode)

		counter = Signal(2, reset=0)

		with m.If(counter == 0):
			m.d.sync += o_wr.eq(1)
			m.d.sync += counter.eq(1)
		with m.Elif(counter == 1):
			m.d.sync += o_wr.eq(0)
			m.d.sync += counter.eq(2)
		with m.Elif(~i_busy):
			with m.If(o_addr == len(psalm_bytes) - 1):
				m.d.sync += self.o_busy.eq(0)
				with m.If(self.i_reset & ~self.o_busy):
					m.d.sync += self.o_busy.eq(1)
					m.d.sync += o_addr.eq(0)
					m.d.sync += counter.eq(0)
			with m.Else():
				m.d.sync += o_addr.eq(o_addr + 1)
				m.d.sync += counter.eq(0)

		if self.fv_mode:
			"""
			Indicator of when Past() is valid
			"""
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			"""
			Assumptions on input pins
			"""
			# i_reset is de-asserted whenever o_busy is asserted
			with m.If(self.o_busy):
				m.d.comb += Assume(~self.i_reset)
			# o_busy is de-asserted for at most 10 consecutive clock cycles before i_reset is asserted
			f_past10_valid = Signal(1, reset=0)
			f_past10_ctr = Signal(range(10), reset=0)
			m.d.sync += f_past10_ctr.eq(f_past10_ctr + 1)
			with m.If(f_past10_ctr == 9):
				m.d.sync += f_past10_ctr.eq(f_past10_ctr)
				m.d.sync += f_past10_valid.eq(1)
			with m.If(f_past10_valid & reduce(lambda a, b: a & b, \
				(((~Past(self.o_busy, i)) & (~Past(self.i_reset, i))) for i in range(1, 11)))):
				m.d.comb += Assume(self.i_reset)
			# The initial data in the read port of the block RAM corresponds to address 0x0
			with m.If(~f_past_valid):
				m.d.comb += Assume(rdport.data == ram[0])
			# The data corresponding to the address applied to the read port of the block RAM always
			# appears one clock cycle later
			with m.If(f_past_valid):
				m.d.comb += Assume(rdport.data == ram[Past(rdport.addr)])
			# i_busy is initially de-asserted
			with m.If(~f_past_valid):
				m.d.comb += Assume(~i_busy)
			# i_busy is never asserted on its own
			with m.If(f_past_valid & (~Past(i_busy)) & ~Past(o_wr)):
				m.d.comb += Assume(~i_busy)
			# When the transmitter is idle, it responds immediately to write requests
			with m.If(f_past_valid & (~Past(i_busy)) & Past(o_wr)):
				m.d.comb += Assume(i_busy)
			# i_busy is asserted for at most 10 consecutive clock cycles
			with m.If(f_past10_valid & reduce(lambda a, b: a & b, \
				(Past(i_busy, i) for i in range(1, 11)))):
				m.d.comb += Assume(~i_busy)

			"""
			Properties of o_busy
			"""
			# o_busy is initially asserted
			with m.If(~f_past_valid):
				m.d.comb += Assert(self.o_busy)
			# o_busy is asserted whenever a transmission is taking place
			with m.If((o_addr != len(psalm_bytes) - 1) | (counter < 2) | i_busy):
				m.d.comb += Assert(self.o_busy)
			# o_busy is de-asserted one clock cycle after the transmission is complete
			with m.If(f_past_valid & (Past(o_addr) == len(psalm_bytes) - 1) & (Past(counter) == 2) & \
				(~Past(i_busy)) & ~Past(self.i_reset)):
				m.d.comb += Assert(~self.o_busy)
			
			"""
			Properties of o_addr
			"""
			# o_addr is initially zero
			with m.If(~f_past_valid):
				m.d.comb += Assert(o_addr == 0)
			# o_addr remains stable during transmission
			with m.If(f_past_valid & ((Past(counter) < 2) | Past(i_busy))):
				m.d.comb += Assert(Stable(o_addr))
			# Except for the last byte, o_addr increments by 1 at the end of each transmission
			with m.If(f_past_valid & (Past(o_addr) != len(psalm_bytes) - 1) & (Past(counter) == 2) & \
				~Past(i_busy)):
				m.d.comb += Assert(o_addr == Past(o_addr) + 1)
			# For the last byte, o_addr is set to 0 at the end of the transmission when i_reset is
			# asserted
			with m.If(f_past_valid & (Past(o_addr) == len(psalm_bytes) - 1) & (Past(counter) == 2) & \
				(~Past(i_busy)) & Past(self.i_reset)):
				m.d.comb += Assert(o_addr == 0)

			"""
			Properties of i_data
			"""
			# Except when counter is zero, i_data should contain the data corresponding to the given
			# address
			with m.If(counter != 0):
				m.d.comb += Assert(i_data == ram[o_addr])

			"""
			Properties of o_wr
			"""
			# o_wr is de-asserted whenever i_busy is asserted
			with m.If(i_busy):
				m.d.comb += Assert(~o_wr)
			# o_wr is asserted precisely when counter is 1, and de-asserted otherwise
			with m.If(counter == 1):
				m.d.comb += Assert(o_wr)
			with m.Else():
				m.d.comb += Assert(~o_wr)

			"""
			Properties of counter
			"""
			# Counter is always counting up when it is less than 2
			with m.If(f_past_valid & (Past(counter) < 2)):
				m.d.comb += Assert(counter == Past(counter) + 1)
			# Counter remains stable at 2 so long as the transmitter is busy
			with m.If(f_past_valid & (Past(counter) == 2) & Past(i_busy)):
				m.d.comb += Assert(Stable(counter))
			# Except for the last byte, counter resets to 0 as soon as the transmitter is idle
			with m.If(f_past_valid & (Past(o_addr) != len(psalm_bytes) - 1) & (Past(counter) == 2) & \
				~Past(i_busy)):
				m.d.comb += Assert(counter == 0)
			# For the last byte, counter resets to 0 once transmitter is idle as soon as i_reset is
			# asserted
			with m.If(f_past_valid & (Past(o_addr) == len(psalm_bytes) - 1) & (Past(counter) == 2) & \
				(~Past(i_busy)) & Past(self.i_reset)):
				m.d.comb += Assert(counter == 0)

		return m

class MemTXDemo(Elaboratable):
	"""
	Demo driver for MemTX
	"""
	def elaborate(self, platform):
		if platform is None:
			raise ValueError('MemTXDemo does not support simulation!')
		if platform == 'formal':
			raise ValueError('MemTXDemo does not support formal verification!')
		m = Module()
		m.submodules.memtx = memtx = MemTX()
		counter = Signal(30)
		m.d.sync += memtx.i_reset.eq(0)
		m.d.sync += counter.eq(counter + 1)
		with m.If(counter == 0x3FFFFFFF):
			m.d.sync += memtx.i_reset.eq(1)
		return m

if __name__ == '__main__':
	"""
	Sanity Check
	"""
	# class Ctr32(Elaboratable):
	# 	def elaborate(self, platform):
	# 		if platform is None:
	# 			raise ValueError('Ctr32 does not support simulation!')
	# 		if platform == 'formal':
	# 			raise ValueError('Ctr32 does not support formal verification!')
	# 		m = Module()
	# 		ctr = Signal(32, reset=0)
	# 		m.d.sync += ctr.eq(ctr + 1)
	# 		m.d.comb += platform.request('led', 0).o.eq(ctr >= 0x7FFFFFFF)
	# 		m.d.comb += platform.request('led', 1).o.eq(ctr >= 0x7FFFFFFF)
	# 		m.d.comb += platform.request('led', 2).o.eq(ctr >= 0x7FFFFFFF)
	# 		m.d.comb += platform.request('led', 3).o.eq(ctr >= 0x7FFFFFFF)
	# 		m.d.comb += platform.request('led', 4).o.eq(ctr >= 0x7FFFFFFF)
	# 		m.d.comb += platform.request('led', 5).o.eq(ctr >= 0x7FFFFFFF)
	# 		m.d.comb += platform.request('led', 6).o.eq(ctr >= 0x7FFFFFFF)
	# 		m.d.comb += platform.request('led', 7).o.eq(ctr >= 0x7FFFFFFF)
	# 		return m
	# VersaECP5Platform().build(Ctr32(), do_program=True)

	"""
	Simulation
	"""
	m = Module()
	m.submodules.memtx = memtx = MemTX()

	sim = Simulator(m)

	def process():
		for i in range(20000):
			yield

	sim.add_clock(1e-8)
	sim.add_sync_process(process)
	with sim.write_vcd('memtx.vcd', 'memtx.gtkw', traces=memtx.ports()):
		sim.run()

	"""
	Formal Verification
	"""
	class MemTXTest(FHDLTestCase):
		def test_memtx(self):
			self.assertFormal(MemTX(fv_mode=True), mode='prove', depth=18)
	MemTXTest().test_memtx()

	"""
	Build
	"""
	VersaECP5Platform().build(MemTXDemo(), do_program=True)