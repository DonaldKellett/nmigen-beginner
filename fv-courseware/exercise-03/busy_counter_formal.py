from nmigen import *
from nmigen.asserts import Assert, Assume, Past
from nmigen.cli import main_parser, main_runner

__all__ = ["BusyCounter"]

"""
Busy counter with formal verification
See slides 76-79 in
https://zipcpu.com/tutorial/class-verilog.pdf
"""

class BusyCounter(Elaboratable):
	def __init__(self, fv_mode = False):
		self.fv_mode = fv_mode
		self.i_reset = Signal(1, reset=0)
		self.i_start_signal = Signal(1, reset=0)
		self.counter = Signal(16, reset=0)
		self.o_busy = Signal(1, reset=0)
	def ports(self):
		return [
			self.i_reset,
			self.i_start_signal,
			self.counter,
			self.o_busy
		]
	def elaborate(self, platform):
		m = Module()
		MAX_AMOUNT = Const(22)
		with m.If(self.i_reset):
			m.d.sync += self.counter.eq(0)
		with m.Elif(self.i_start_signal & (self.counter == 0)):
			m.d.sync += self.counter.eq(MAX_AMOUNT - 1)
		with m.Elif(self.counter != 0):
			m.d.sync += self.counter.eq(self.counter - 1)
		m.d.sync += self.o_busy.eq((~self.i_reset) & \
			((self.i_start_signal & (self.counter == 0)) | \
			(self.counter > 1)))
		if self.fv_mode:
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)
			m.d.comb += Assert(self.counter < MAX_AMOUNT)
			with m.If(f_past_valid & Past(self.i_start_signal) & Past(self.o_busy)):
				m.d.comb += Assume(self.i_start_signal)
			with m.Elif(f_past_valid & Past(self.i_start_signal) & ~Past(self.o_busy)):
				m.d.comb += Assume(~self.i_start_signal)
			m.d.comb += Assert(self.o_busy == (self.counter != 0))
			with m.If(f_past_valid & Past(self.counter) != 0):
				m.d.comb += Assert(self.counter < Past(self.counter))
		return m

if __name__ == "__main__":
	parser = main_parser()
	args = parser.parse_args()

	m = Module()
	m.submodules.counter = counter = BusyCounter(True)

	main_runner(parser, args, m, ports = counter.ports())