from nmigen import *
from nmigen.back.pysim import *
from nmigen.asserts import *
from nmigen.cli import main_parser, main_runner
from lfsr_fib import *

__all__ = ["DblPipe"]

"""
Second part of Exercise 4 in https://zipcpu.com/tutorial/class-verilog.pdf
, slides 103-106
"""

class DblPipe(Elaboratable):
	def __init__(self, i_ce, i_data, o_data, fv_mode = False):
		self.i_ce = i_ce
		self.i_data = i_data
		self.o_data = o_data
		self.a_data = Signal(1)
		self.b_data = Signal(1)
		self.fv_mode = fv_mode
	def ports(self):
		return [
			self.i_ce,
			self.i_data,
			self.o_data,
			self.a_data,
			self.b_data
		]
	def elaborate(self, platform):
		m = Module()
		m.submodules.one = LFSRFib(0, self.i_ce, \
			self.i_data, self.a_data, fv_mode = self.fv_mode)
		m.submodules.two = LFSRFib(0, self.i_ce, \
			self.i_data, self.b_data, fv_mode = self.fv_mode)
		m.d.sync += self.o_data.eq(self.a_data ^ self.b_data)
		if self.fv_mode:
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			# Neither sregs in one or two will change as long as CE is low
			# (since reset is always de-asserted)
			with m.If(f_past_valid & (~Past(self.i_ce))):
				m.d.comb += Assert(m.submodules.one.sreg == \
					Past(m.submodules.one.sreg))
				m.d.comb += Assert(m.submodules.two.sreg == \
					Past(m.submodules.two.sreg))

			# The sregs of one and two are both initialized to the same
			# value
			with m.If(~f_past_valid):
				m.d.comb += Assert(m.submodules.one.sreg == \
					m.submodules.two.sreg)

			# When CE is high in a given clock cycle, given that the sregs
			# of one and two have the same value, their values in the next
			# clock cycle are also equal
			with m.If(f_past_valid & Past(self.i_ce) & \
				(Past(m.submodules.one.sreg) == \
				Past(m.submodules.two.sreg))):
				m.d.comb += Assert(m.submodules.one.sreg == \
					m.submodules.two.sreg)

			# Hence, the sregs in one and two are equal for all time ...
			m.d.comb += Assert(m.submodules.one.sreg == \
				m.submodules.two.sreg)

			# ... and thus o_data is forever zero!
			m.d.comb += Assert(self.o_data == 0)

		return m

# Formal Verification
if __name__ == "__main__":
	parser = main_parser()
	args = parser.parse_args()

	m = Module()
	i_ce = Signal(1, reset=1)
	i_data = Signal(1, reset=0)
	o_data = Signal(1)
	m.submodules.dblpipe = dblpipe = DblPipe(i_ce, i_data, o_data, \
		fv_mode = True)

	main_runner(parser, args, m, ports = dblpipe.ports())

# Simulation
# if __name__ == "__main__":
# 	m = Module()
# 	i_ce = Signal(1, reset=1)
# 	i_data = Signal(1, reset=0)
# 	o_data = Signal(1)
# 	m.submodules.dblpipe = dblpipe = DblPipe(i_ce, i_data, o_data)

# 	sim = Simulator(m)

# 	def process():
# 		for i in range(1000):
# 			yield

# 	sim.add_clock(1e-8)
# 	sim.add_sync_process(process)
# 	with sim.write_vcd('dblpipe.vcd', 'dblpipe.gtkw', \
# 		traces = dblpipe.ports()):
# 		sim.run()
