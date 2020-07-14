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

from txuart import *

__all__ = ["HelloWorld", "VersaECP5Platform"]

"""
Hello World top-level for RS-232 transmitter, this time formally verified
to behave correctly
See https://zipcpu.com/tutorial/lsn-05-serialtx.pdf for more details
"""

class HelloWorld(Elaboratable):
	def __init__(self, msg = "Hello World!", fv_mode = False):
		self.i_busy = Signal(1, reset=0)
		self.o_wr = Signal(1, reset=0)
		self.msg = "%s\n" % msg
		self.o_data = Signal(8, reset=ord(self.msg[0]))
		self.fv_mode = fv_mode
	def ports(self):
		return [
			self.i_busy,
			self.o_wr,
			self.o_data
		]
	def elaborate(self, platform):
		m = Module()

		o_uart_tx = Signal(1, reset=1)

		state = Signal(range(len(self.msg)), reset=0)

		if platform is not None and platform != "formal":
			o_uart_tx = platform.request("uart").tx.o
		
		m.submodules.txuart = txuart = TXUART(self.o_wr, self.o_data, self.i_busy, \
			o_uart_tx, self.fv_mode)

		m.d.comb += self.o_wr.eq(~self.i_busy)

		with m.FSM():
			for i in range(len(self.msg)):
				with m.State(str(i)):
					m.next = str(i)
					with m.If(self.o_wr):
						m.next = str((i + 1) % len(self.msg))
						if i == len(self.msg) - 1:
							m.d.sync += state.eq(0)
						else:
							m.d.sync += state.eq(state + 1)
						m.d.sync += self.o_data.eq(ord(self.msg[(i + 1) % len(self.msg)]))

		if self.fv_mode:
			"""
			Indicator of whether Past() is valid
			"""
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			"""
			Assume there is a reasonable upper bound on the consecutive number of clock
			cycles that i_busy is asserted, say, 10 * CLOCKS_PER_BAUD
			This is required for some assertions to pass k-induction
			"""
			# CLOCKS_PER_BAUD = 4 in simulation (see txuart.py)
			CLOCKS_PER_BAUD = 4

			f_past10n_valid = Signal(1, reset=0)
			f_past10n_ctr = Signal(range(10 * CLOCKS_PER_BAUD), reset=0)
			m.d.sync += f_past10n_ctr.eq(f_past10n_ctr + 1)
			with m.If(f_past10n_ctr == 10 * CLOCKS_PER_BAUD - 1):
				m.d.sync += f_past10n_ctr.eq(f_past10n_ctr)
				m.d.sync += f_past10n_valid.eq(1)

			with m.If(f_past10n_valid & reduce(lambda a, b: a & b, \
				(Past(self.i_busy, i) for i in range(1, 10 * CLOCKS_PER_BAUD + 1)))):
				m.d.comb += Assume(~self.i_busy)

			"""
			Properties of o_wr
			"""
			# o_wr is never asserted when i_busy is asserted
			with m.If(self.i_busy):
				m.d.comb += Assert(~self.o_wr)

			"""
			Properties of o_data
			"""
			# o_data holds the correct byte in each respective state
			with m.Switch(state):
				for i in range(len(self.msg)):
					with m.Case(i):
						m.d.comb += Assert(self.o_data == ord(self.msg[i]))

			"""
			Properties regarding state
			"""
			# Initial state is zero (= transmit first character)
			with m.If(~f_past_valid):
				m.d.comb += Assert(state == 0)
			# o_wr triggers state transitions, and state transitions are correct
			with m.If(f_past_valid & Past(self.o_wr)):
				m.d.comb += Assert(state == ((Past(state) + 1) % len(self.msg)))

		return m

if __name__ == "__main__":
	"""
	Simulation
	"""
	m = Module()
	m.submodules.helloworld = helloworld = HelloWorld()

	sim = Simulator(m)

	def process():
		for i in range(1000):
			yield

	sim.add_clock(1e-8)
	sim.add_sync_process(process)

	with sim.write_vcd('helloworld.vcd', 'helloworld.gtkw', traces=helloworld.ports()):
		sim.run()

	"""
	Formal Verification
	"""
	class HelloWorldTest(FHDLTestCase):
		def test_helloworld(self):
			self.assertFormal(HelloWorld(fv_mode=True), mode='prove', depth=66)
	HelloWorldTest().test_helloworld()

	"""
	Build
	"""
	VersaECP5Platform().build(HelloWorld("FPGA programming with nMigen is fun"), do_program=True)