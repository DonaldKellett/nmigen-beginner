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

__all__ = ["ChgDetector"]

"""
Change detector for txdata
See https://zipcpu.com/tutorial/lsn-06-txdata.pdf for more details
"""

class ChgDetector(Elaboratable):
	def __init__(self, i_data, o_stb, o_data, i_busy, fv_mode=False):
		self.i_data = i_data
		self.o_stb = o_stb
		self.o_data = o_data
		self.i_busy = i_busy
		self.fv_mode = fv_mode
	def ports(self):
		return [
			self.i_data,
			self.o_stb,
			self.o_data,
			self.i_busy
		]
	def elaborate(self, platform):
		m = Module()

		m.d.sync += self.o_stb.eq(0)

		stb_past = Signal(1)
		m.d.comb += stb_past.eq(self.o_stb)

		with m.If(stb_past):
				m.d.sync += self.o_stb.eq(0)
		with m.Elif((~self.i_busy) & (self.i_data != self.o_data)):
			m.d.sync += self.o_stb.eq(1)
			m.d.sync += self.o_data.eq(self.i_data)

		if self.fv_mode:
			"""
			Indicator of when Past() is valid
			"""
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			"""
			Assumptions on input behavior
			"""
			# Assume i_busy is initially de-asserted
			with m.If(~f_past_valid):
				m.d.comb += Assume(~self.i_busy)
			# Assume i_busy does not get asserted on its own without a corresponding
			# o_stb in the previous clock cycle
			with m.If(f_past_valid & (~Past(self.i_busy)) & ~Past(self.o_stb)):
				m.d.comb += Assume(~self.i_busy)
			# Given that i_busy was de-asserted in the previous clock cycle, if o_stb was
			# asserted in the previous clock cycle then i_busy should be asserted in this
			# clock cycle, i.e. responses to strobe requests are immediate when idle
			with m.If(f_past_valid & (~Past(self.i_busy)) & Past(self.o_stb)):
				m.d.comb += Assume(self.i_busy)

			"""
			Properties of o_stb
			"""
			# o_stb is initially de-asserted
			with m.If(~f_past_valid):
				m.d.comb += Assert(~self.o_stb)
			# o_stb is never asserted when i_busy is asserted
			with m.If(self.i_busy):
				m.d.comb += Assert(~self.o_stb)
			# If there was no change to the data in the previous clock cycle then
			# o_stb is de-asserted for this clock cycle
			with m.If(f_past_valid & (Past(self.i_data) == Past(self.o_data))):
				m.d.comb += Assert(~self.o_stb)
			# Given that i_busy and o_stb were de-asserted in the previous clock cycle,
			# if there was a change to the data in the previous clock cycle then o_stb
			# is asserted in this clock cycle
			with m.If(f_past_valid & (~Past(self.i_busy)) & (~Past(self.o_stb)) & \
				(Past(self.i_data) != Past(self.o_data))):
				m.d.comb += Assert(self.o_stb)

			"""
			Properties of o_data
			"""
			# o_data is initially zero
			with m.If(~f_past_valid):
				m.d.comb += Assert(self.o_data == 0)
			# Given that i_busy and o_stb were de-asserted in the previous clock cycle,
			# whatever value i_data had in the previous clock cycle, o_data now contains
			# that value in this clock cycle
			with m.If(f_past_valid & (~Past(self.i_busy)) & ~Past(self.o_stb)):
				m.d.comb += Assert(self.o_data == Past(self.i_data))
			# o_data should remain stable when o_stb or i_busy are asserted even if i_data
			# changes
			with m.If(f_past_valid & (Past(self.i_busy) | Past(self.o_stb))):
				m.d.comb += Assert(Stable(self.o_data))


		return m

if __name__ == "__main__":
	"""
	Formal Verification
	No point in simulating/building such a trivial design
	"""
	class ChgDetectorTest(FHDLTestCase):
		def test_chgdetector(self):
			i_data = Signal(32, reset=0)
			o_stb = Signal(1, reset=0)
			o_data = Signal(32, reset=0)
			i_busy = Signal(1, reset=0)
			chgdetector = ChgDetector(i_data, o_stb, o_data, i_busy, fv_mode=True)
			self.assertFormal(chgdetector, mode='prove')
	ChgDetectorTest().test_chgdetector()