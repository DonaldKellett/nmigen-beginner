from nmigen import *
from nmigen.back.pysim import *

__all__ = ["LFSRGal"]

"""
Exercise 5 (slides 107-108) of
https://zipcpu.com/tutorial/class-verilog.pdf
"""

class LFSRGal(Elaboratable):
	def __init__(self, i_reset, i_ce, i_in, o_bit, fv_mode = False):
		self.i_reset = i_reset
		self.i_ce = i_ce
		self.i_in = i_in
		self.o_bit = o_bit
		self.sreg = Signal(8, reset=0x80)
		self.fv_mode = fv_mode
	def ports(self):
		return [
			self.i_reset,
			self.i_ce,
			self.i_in,
			self.o_bit,
			self.sreg
		]
	def elaborate(self, platform):
		m = Module()
		
		TAPS = Const(0xb4)

		with m.If(self.i_reset):
			m.d.sync += self.sreg.eq(0x80)
		with m.Elif(self.i_ce):
			with m.If(self.sreg[0]):
				m.d.sync += self.sreg.eq(Cat(self.sreg[1:], self.i_in) ^ \
					TAPS)
			with m.Else():
				m.d.sync += self.sreg.eq(Cat(self.sreg[1:], self.i_in))

		m.d.comb += self.o_bit.eq(self.sreg[0])

		return m

# Simulation
if __name__ == "__main__":
	m = Module()
	i_reset = Signal(1, reset=0)
	i_ce = Signal(1, reset=1)
	i_in = Signal(1, reset=0)
	o_bit = Signal(1)
	m.submodules.lfsr_gal = lfsr_gal = LFSRGal(i_reset, i_ce, i_in, o_bit)

	sim = Simulator(m)

	def process():
		for i in range(1000):
			yield

	sim.add_clock(1e-8)
	sim.add_sync_process(process)
	with sim.write_vcd('lfsr_gal.vcd', 'lfsr_gal.gtkw', \
		traces = lfsr_gal.ports()):
		sim.run()