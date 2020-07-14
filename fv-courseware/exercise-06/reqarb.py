from nmigen import *
from nmigen.asserts import *
from nmigen.cli import main_parser, main_runner

__all__ = ['ReqArb']

class ReqArb(Elaboratable):
	def __init__(self, i_reset, \
		i_a_req, i_a_data, o_a_busy, \
		i_b_req, i_b_data, o_b_busy, \
		o_req, o_data, i_busy, fv_mode = False):
		self.i_reset = i_reset
		self.i_a_req = i_a_req
		self.i_a_data = i_a_data
		self.o_a_busy = o_a_busy
		self.i_b_req = i_b_req
		self.i_b_data = i_b_data
		self.o_b_busy = o_b_busy
		self.o_req = o_req
		self.o_data = o_data
		self.i_busy = i_busy
		self.a_is_the_owner = Signal(1, reset=0)
		self.fv_mode = fv_mode
	def ports(self):
		return [
			self.i_reset,
			self.i_a_req,
			self.i_a_data,
			self.o_a_busy,
			self.i_b_req,
			self.i_b_data,
			self.o_b_busy,
			self.o_req,
			self.o_data,
			self.i_busy,
			self.a_is_the_owner
		]
	def elaborate(self, platform):
		m = Module()

		with m.If(self.i_reset):
			m.d.sync += self.a_is_the_owner.eq(0)
		with m.Elif(self.i_a_req & ~self.i_b_req):
			m.d.sync += self.a_is_the_owner.eq(1)
		with m.Elif(self.i_b_req & ~self.i_a_req):
			m.d.sync += self.a_is_the_owner.eq(0)

		m.d.comb += self.o_a_busy.eq((~self.a_is_the_owner) | self.i_busy)

		m.d.comb += self.o_b_busy.eq(self.a_is_the_owner | self.i_busy)

		m.d.comb += self.o_req.eq(Mux(self.a_is_the_owner, self.i_a_req, self.i_b_req))
		m.d.comb += self.o_data.eq(Mux(self.a_is_the_owner, self.i_a_data, self.i_b_data))

		if self.fv_mode:
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			with m.If((~f_past_valid) | Past(self.i_reset)):
				m.d.comb += Assert(~self.a_is_the_owner)
				m.d.comb += Assert(self.o_a_busy)
				m.d.comb += Assert(self.o_b_busy == self.i_busy)
				m.d.comb += Assert(self.o_req == self.i_b_req)
				m.d.comb += Assert(self.o_data == self.i_b_data)

			# 1. No data will be lost, no requests will be dropped
			with m.If(f_past_valid):
				with m.If(Past(self.o_a_busy)):
					m.d.comb += Assume(self.i_a_req == Past(self.i_a_req))
					m.d.comb += Assume(self.i_a_data == Past(self.i_a_data))
				with m.If(Past(self.o_b_busy)):
					m.d.comb += Assume(self.i_b_req == Past(self.i_b_req))
					m.d.comb += Assume(self.i_b_data == Past(self.i_b_data))

			# 2. Only one source will ever have access to the channel at any given time
			m.d.comb += Assert(self.o_a_busy | self.o_b_busy)

			# 3. All requests will go through
			with m.If(~self.o_a_busy):
				m.d.comb += Assert(self.a_is_the_owner)
				m.d.comb += Assert(~self.i_busy)
				m.d.comb += Assert(self.o_b_busy)
				m.d.comb += Assert(self.o_req == self.i_a_req)
				m.d.comb += Assert(self.o_data == self.i_a_data)
			with m.If(~self.o_b_busy):
				m.d.comb += Assert(~self.a_is_the_owner)
				m.d.comb += Assert(~self.i_busy)
				m.d.comb += Assert(self.o_a_busy)
				m.d.comb += Assert(self.o_req == self.i_b_req)
				m.d.comb += Assert(self.o_data == self.i_b_data)

		return m

# Formal Verification
if __name__ == "__main__":
	parser = main_parser()
	args = parser.parse_args()

	m = Module()
	i_reset = Signal(1, reset=0)
	i_a_req = Signal(1, reset=0)
	i_a_data = Signal(1, reset=0)
	o_a_busy = Signal(1)
	i_b_req = Signal(1, reset=0)
	i_b_data = Signal(1, reset=0)
	o_b_busy = Signal(1)
	o_req = Signal(1)
	o_data = Signal(1)
	i_busy = Signal(1, reset=0)
	m.submodules.reqarb = reqarb = ReqArb(i_reset, \
		i_a_req, i_a_data, o_a_busy, \
		i_b_req, i_b_data, o_b_busy, \
		o_req, o_data, i_busy, fv_mode = True)

	main_runner(parser, args, m, ports = reqarb.ports())