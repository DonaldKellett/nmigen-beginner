from nmigen import *
from nmigen.back.pysim import *
from nmigen.asserts import *
from nmigen.cli import main_parser, main_runner
from functools import reduce

__all__ = ["LFSRFib"]

"""
First part of Exercise 4 in https://zipcpu.com/tutorial/class-verilog.pdf
, slides 103-106
"""

class LFSRFib(Elaboratable):
	def __init__(self, i_reset, i_ce, i_in, o_bit, fv_mode = False):
		self.i_reset = i_reset
		self.i_ce = i_ce
		self.i_in = i_in
		self.o_bit = o_bit
		self.sreg = Signal(8, reset=1)
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
		TAPS = Const(0x2d)
		with m.If(self.i_reset):
			m.d.sync += self.sreg.eq(1)
		with m.Elif(self.i_ce):
			m.d.sync += self.sreg[:-1].eq(self.sreg[1:])
			m.d.sync += self.sreg[-1].eq(reduce(lambda a, b: a ^ b, \
				self.sreg & TAPS) ^ self.i_in)
		m.d.comb += self.o_bit.eq(self.sreg[0])
		if self.fv_mode:
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			# If i_in is forever zero then sreg will never be completely zero
			# We prove this in two parts:
			# 1) sreg is initially nonzero
			# 2) In any clock cycle, if i_in is zero and sreg is nonzero then
			#    sreg is also nonzero in the next clock cycle
			with m.If(~f_past_valid):
				m.d.comb += Assert(self.sreg != 0)
			with m.Elif(f_past_valid & (~Past(self.i_in)) & Past(self.sreg) != 0):
				m.d.comb += Assert(self.sreg != 0)

			# If sreg is ever zero then sreg will remain zero until the clock
			# after i_in is true
			# Hidden assumptions (not mentioned in the exercises):
			# 1) The reset signal is de-asserted; otherwise sreg will
			#    unconditionally become 1 on the next clock cycle regardless
			#    of i_in
			# 2) i_ce is asserted; otherwise sreg will remain zero on the
			#    next clock cycle regardless of i_in
			with m.If(f_past_valid & (Past(self.sreg) == 0) & \
				(~Past(self.i_reset)) & Past(self.i_ce)):
				with m.If(~Past(self.i_in)):
					m.d.comb += Assert(self.sreg == 0)
				with m.Else():
					m.d.comb += Assert(self.sreg != 0)

		return m

# Formal Verification
if __name__ == "__main__":
	parser = main_parser()
	args = parser.parse_args()

	m = Module()
	i_reset = Signal(1, reset=0)
	i_ce = Signal(1, reset=1)
	i_in = Signal(1, reset=0)
	o_bit = Signal(1)
	m.submodules.lfsr_fib = lfsr_fib = LFSRFib(i_reset, i_ce, i_in, \
		o_bit, fv_mode = True)

	main_runner(parser, args, m, ports = lfsr_fib.ports())

# Simulation
# if __name__ == "__main__":
# 	m = Module()
# 	i_reset = Signal(1, reset=0)
# 	i_ce = Signal(1, reset=1)
# 	i_in = Signal(1, reset=0)
# 	o_bit = Signal(1)
# 	m.submodules.lfsr_fib = lfsr_fib = LFSRFib(i_reset, i_ce, i_in, \
# 		o_bit)

# 	sim = Simulator(m)

# 	def process():
# 		for i in range(1000):
# 			yield

# 	sim.add_clock(1e-8)
# 	sim.add_sync_process(process)
# 	with sim.write_vcd("lfsr_fib.vcd", "lfsr_fib.gtkw", traces=lfsr_fib.ports()):
# 		sim.run()
