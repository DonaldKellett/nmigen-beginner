from nmigen import *
from nmigen.asserts import Assert
from nmigen.cli import main_parser, main_runner

__all__ = ["Counter"]

"""
Simple counter with formal verification
See slides 50-60 in
https://zipcpu.com/tutorial/class-verilog.pdf
"""

class Counter(Elaboratable):
	def __init__(self, fv_mode = False):
		self.fv_mode = fv_mode
		self.i_start_signal = Signal(1, reset=0)
		self.counter = Signal(16)
		self.o_busy = Signal(1, reset=0)
	def ports(self):
		return [
			self.i_start_signal,
			self.counter,
			self.o_busy
		]
	def elaborate(self, platform):
		m = Module()
		MAX_AMOUNT = Const(22)
		with m.If(self.i_start_signal & (self.counter == 0)):
			m.d.sync += self.counter.eq(MAX_AMOUNT - 1)
		with m.Elif(self.counter != 0):
			m.d.sync += self.counter.eq(self.counter - 1)
		m.d.comb += self.o_busy.eq(self.counter != 0)
		if self.fv_mode:
			m.d.comb += Assert(self.counter < MAX_AMOUNT)
		return m

if __name__ == "__main__":
	parser = main_parser()
	args = parser.parse_args()

	m = Module()
	m.submodules.counter = counter = Counter(True)

	main_runner(parser, args, m, ports = counter.ports())