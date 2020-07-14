from nmigen import *
from nmigen.back.pysim import *
from nmigen.asserts import *
from nmigen.test.utils import *
from nmigen.cli import main_parser, main_runner
from lfsr_fib import *
from lfsr_gal import *
from functools import reduce

__all__ = ["LFSREquiv"]

"""
Exercise 5 (slides 107-108) of
https://zipcpu.com/tutorial/class-verilog.pdf

To run the formal verification in this script, run
$ python ./lfsr_equiv.py
If no output is generated then this means the formal verification has passed
"""

class LFSREquiv(Elaboratable):
	def __init__(self, i_reset, i_ce, i_in, o_bit, fv_mode = False):
		self.i_reset = i_reset
		self.i_ce = i_ce
		self.i_in = i_in
		self.fib_bit = Signal(1)
		self.gal_bit = Signal(1)
		self.o_bit = o_bit
		self.fv_mode = fv_mode
	def ports(self):
		return [
			self.i_reset,
			self.i_ce,
			self.i_in,
			self.fib_bit,
			self.gal_bit,
			self.o_bit
		]
	def elaborate(self, platform):
		m = Module()

		m.submodules.fib = fib = LFSRFib(self.i_reset, self.i_ce, \
			self.i_in, self.fib_bit, self.fv_mode)
		m.submodules.gal = gal = LFSRGal(self.i_reset, self.i_ce, \
			self.i_in, self.gal_bit, self.fv_mode)

		m.d.comb += self.o_bit.eq(self.fib_bit ^ self.gal_bit)

		if self.fv_mode:
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			with m.If(~f_past_valid):
				m.d.comb += Assert(fib.sreg[0] == gal.sreg[0])
				m.d.comb += Assert(fib.sreg[1] == gal.sreg[1])
				m.d.comb += Assert(fib.sreg[2] == gal.sreg[2])
				m.d.comb += Assert((fib.sreg[3] ^ gal.sreg[3]) == gal.sreg[0])
				m.d.comb += Assert((fib.sreg[4] ^ gal.sreg[4]) == gal.sreg[1])
				m.d.comb += Assert((fib.sreg[5] ^ gal.sreg[5]) == (gal.sreg[2] ^ gal.sreg[0]))
				m.d.comb += Assert((fib.sreg[6] ^ gal.sreg[6]) == (gal.sreg[3] ^ gal.sreg[1]))
				m.d.comb += Assert((fib.sreg[7] ^ gal.sreg[7]) == (gal.sreg[4] ^ gal.sreg[2]))
			with m.Elif((Past(fib.sreg)[0] == Past(gal.sreg)[0]) & \
				(Past(fib.sreg)[1] == Past(gal.sreg)[1]) & \
				(Past(fib.sreg)[2] == Past(gal.sreg)[2]) & \
				((Past(fib.sreg)[3] ^ Past(gal.sreg)[3]) == Past(gal.sreg)[0]) & \
				((Past(fib.sreg)[4] ^ Past(gal.sreg)[4]) == Past(gal.sreg)[1]) & \
				((Past(fib.sreg)[5] ^ Past(gal.sreg)[5]) == (Past(gal.sreg)[2] ^ Past(gal.sreg)[0])) & \
				((Past(fib.sreg)[6] ^ Past(gal.sreg)[6]) == (Past(gal.sreg)[3] ^ Past(gal.sreg)[1])) & \
				((Past(fib.sreg)[7] ^ Past(gal.sreg)[7]) == (Past(gal.sreg)[4] ^ Past(gal.sreg)[2]))):
				m.d.comb += Assert(fib.sreg[0] == gal.sreg[0])
				m.d.comb += Assert(fib.sreg[1] == gal.sreg[1])
				m.d.comb += Assert(fib.sreg[2] == gal.sreg[2])
				m.d.comb += Assert((fib.sreg[3] ^ gal.sreg[3]) == gal.sreg[0])
				m.d.comb += Assert((fib.sreg[4] ^ gal.sreg[4]) == gal.sreg[1])
				m.d.comb += Assert((fib.sreg[5] ^ gal.sreg[5]) == (gal.sreg[2] ^ gal.sreg[0]))
				m.d.comb += Assert((fib.sreg[6] ^ gal.sreg[6]) == (gal.sreg[3] ^ gal.sreg[1]))
				m.d.comb += Assert((fib.sreg[7] ^ gal.sreg[7]) == (gal.sreg[4] ^ gal.sreg[2]))

			# Circuit Invariant - the property that holds between clock cycles
			m.d.comb += Assert(fib.sreg[0] == gal.sreg[0])
			m.d.comb += Assert(fib.sreg[1] == gal.sreg[1])
			m.d.comb += Assert(fib.sreg[2] == gal.sreg[2])
			m.d.comb += Assert((fib.sreg[3] ^ gal.sreg[3]) == gal.sreg[0])
			m.d.comb += Assert((fib.sreg[4] ^ gal.sreg[4]) == gal.sreg[1])
			m.d.comb += Assert((fib.sreg[5] ^ gal.sreg[5]) == (gal.sreg[2] ^ gal.sreg[0]))
			m.d.comb += Assert((fib.sreg[6] ^ gal.sreg[6]) == (gal.sreg[3] ^ gal.sreg[1]))
			m.d.comb += Assert((fib.sreg[7] ^ gal.sreg[7]) == (gal.sreg[4] ^ gal.sreg[2]))

			# Therefore, our desired property follows immediately. Q.E.D.
			m.d.comb += Assert(~self.o_bit)

		return m

# Simulation
# if __name__ == "__main__":
# 	m = Module()
# 	i_reset = Signal(1, reset=0)
# 	i_ce = Signal(1, reset=1)
# 	i_in = Signal(1, reset=0)
# 	o_bit = Signal(1)
# 	m.submodules.lfsr_equiv = lfsr_equiv = LFSREquiv(i_reset, i_ce, i_in, \
# 		o_bit)

# 	sim = Simulator(m)

# 	def process():
# 		for i in range(1000):
# 			yield

# 	sim.add_clock(1e-8)
# 	sim.add_sync_process(process)

# 	with sim.write_vcd('lfsr_equiv.vcd', 'lfsr_equiv.gtkw', \
# 		traces = lfsr_equiv.ports()):
# 		sim.run()

# Formal Verification
class LFSREquivTest(FHDLTestCase):
	def test_lfsr_equiv(self):
		i_reset = Signal(1, reset=0)
		i_ce = Signal(1, reset=1)
		i_in = Signal(1, reset=0)
		o_bit = Signal(1)
		lfsr_equiv = LFSREquiv(i_reset, i_ce, i_in, o_bit, fv_mode = True)
		self.assertFormal(lfsr_equiv, mode="prove")
LFSREquivTest().test_lfsr_equiv()