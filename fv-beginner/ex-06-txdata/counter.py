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

__all__ = ['Counter']

"""
Event counter for txdata
See https://zipcpu.com/tutorial/lsn-06-txdata.pdf for more details
"""

class Counter(Elaboratable):
	def __init__(self, i_reset, i_event, o_counter, fv_mode = False):
		self.i_reset = i_reset
		self.i_event = i_event
		self.o_counter = o_counter
		self.fv_mode = fv_mode
	def ports(self):
		return [self.i_reset, self.i_event, self.o_counter]
	def elaborate(self, platform):
		m = Module()

		with m.If(self.i_reset):
			m.d.sync += self.o_counter.eq(0)
		with m.Elif(self.i_event):
			m.d.sync += self.o_counter.eq(self.o_counter + 1)

		if self.fv_mode:
			"""
			Indicators of when Past() is valid
			"""
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			"""
			Assume there is at least 1 event every 10 clock cycles
			and at least 1 reset every 10 clock cycles for k-induction
			to pass
			"""
			f_past9_valid = Signal(1, reset=0)
			f_past9_ctr = Signal(range(9), reset=0)
			m.d.sync += f_past9_ctr.eq(f_past9_ctr + 1)
			with m.If(f_past9_ctr == 8):
				m.d.sync += f_past9_ctr.eq(f_past9_ctr)
				m.d.sync += f_past9_valid.eq(1)

			with m.If(f_past9_valid & reduce(lambda a, b: a & b, \
				((~Past(self.i_reset, i)) for i in range(1, 10)))):
				m.d.comb += Assume(self.i_reset)
			with m.If(f_past9_valid & reduce(lambda a, b: a & b, \
				((~Past(self.i_event, i)) for i in range(1, 10)))):
				m.d.comb += Assume(self.i_event)

			"""
			Counter properties
			"""
			# Counter is initially zero
			with m.If(~f_past_valid):
				m.d.comb += Assert(self.o_counter == 0)
			# On reset, counter resets to zero on next clock cycle
			with m.If(f_past_valid & Past(self.i_reset)):
				m.d.comb += Assert(self.o_counter == 0)
			# On event, given there is no reset, counter increments by 1
			with m.If(f_past_valid & Past(self.i_event) & ~Past(self.i_reset)):
				m.d.comb += Assert(self.o_counter == (Past(self.o_counter) + 1))

		return m

if __name__ == "__main__":
	"""
	Formal Verification (sanity check)
	No point in simulating/building this trivial design
	"""
	class CounterTest(FHDLTestCase):
		def test_counter(self):
			i_reset = Signal(1, reset=0)
			i_event = Signal(1, reset=0)
			o_counter = Signal(32, reset=0)
			counter = Counter(i_reset, i_event, o_counter, fv_mode=True)
			self.assertFormal(counter, mode='prove', depth=17)
	CounterTest().test_counter()