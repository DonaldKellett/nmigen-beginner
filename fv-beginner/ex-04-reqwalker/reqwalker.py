from nmigen import *
from nmigen.back.pysim import *
from nmigen.asserts import *
from nmigen.test.utils import *
from nmigen.build import *
from nmigen.build import ResourceError
from nmigen.vendor.lattice_ecp5 import *
from nmigen_boards.resources import *

import itertools
import os
import subprocess

__all__ = ["ReqWalker", "VersaECP5Platform"]

"""
LED Walker upon request
Adapted from https://zipcpu.com/tutorial/lsn-04-pipeline.pdf

To run formal verification, run
$ python ./reqwalker.py
No output means the formal verification has passed
"""

class ReqWalker(Elaboratable):
	def __init__(self, fv_mode = False):
		self.leds = Signal(8, reset=0b11111111)
		self.counter = Signal(32, reset=0)
		self.i_req = Signal(1, reset=0)
		self.o_busy = Signal(1)
		self.state = Signal(4, reset=0)
		self.fv_mode = fv_mode
	def ports(self):
		return [
			self.leds,
			self.counter,
			self.i_req,
			self.o_busy,
			self.state
		]
	def elaborate(self, platform):
		m = Module()

		PERIOD = 4

		if platform is not None and platform != "formal":
			self.leds = Cat(*(platform.request("led", i).o for i in range(8)))
			PERIOD = int(platform.default_clk_frequency // 4)
			req_count = Signal(29, reset=0)
			m.d.sync += req_count.eq(req_count + 1)
			m.d.sync += self.i_req.eq(0)
			with m.If(req_count == 0x1FFFFFFF):
				m.d.sync += self.i_req.eq(1)

		m.d.comb += self.o_busy.eq(self.state != 0)

		with m.FSM():
			with m.State('READY'):
				m.next = 'READY'
				m.d.sync += self.leds.eq(0b11111111)
				m.d.sync += self.counter.eq(0)
				with m.If(self.i_req):
					m.next = 'WALK1'
					m.d.sync += self.state.eq(1)
					m.d.sync += self.leds.eq(0b11111110)
			with m.State('WALK1'):
				m.next = 'WALK1'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK2'
					m.d.sync += self.state.eq(2)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11111101)
			with m.State('WALK2'):
				m.next = 'WALK2'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK3'
					m.d.sync += self.state.eq(3)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11111011)
			with m.State('WALK3'):
				m.next = 'WALK3'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK4'
					m.d.sync += self.state.eq(4)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11110111)
			with m.State('WALK4'):
				m.next = 'WALK4'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK5'
					m.d.sync += self.state.eq(5)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11101111)
			with m.State('WALK5'):
				m.next = 'WALK5'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK6'
					m.d.sync += self.state.eq(6)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11011111)
			with m.State('WALK6'):
				m.next = 'WALK6'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK7'
					m.d.sync += self.state.eq(7)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b10111111)
			with m.State('WALK7'):
				m.next = 'WALK7'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK8'
					m.d.sync += self.state.eq(8)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b01111111)
			with m.State('WALK8'):
				m.next = 'WALK8'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK9'
					m.d.sync += self.state.eq(9)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b10111111)
			with m.State('WALK9'):
				m.next = 'WALK9'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK10'
					m.d.sync += self.state.eq(10)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11011111)
			with m.State('WALK10'):
				m.next = 'WALK10'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK11'
					m.d.sync += self.state.eq(11)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11101111)
			with m.State('WALK11'):
				m.next = 'WALK11'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK12'
					m.d.sync += self.state.eq(12)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11110111)
			with m.State('WALK12'):
				m.next = 'WALK12'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK13'
					m.d.sync += self.state.eq(13)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11111011)
			with m.State('WALK13'):
				m.next = 'WALK13'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK14'
					m.d.sync += self.state.eq(14)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11111101)
			with m.State('WALK14'):
				m.next = 'WALK14'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'WALK15'
					m.d.sync += self.state.eq(15)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11111110)
			with m.State('WALK15'):
				m.next = 'WALK15'
				m.d.sync += self.counter.eq(self.counter + 1)
				with m.If(self.counter == PERIOD - 1):
					m.next = 'READY'
					m.d.sync += self.state.eq(0)
					m.d.sync += self.counter.eq(0)
					m.d.sync += self.leds.eq(0b11111111)

		if self.fv_mode:
			"""
			Indicators of when Past() is valid
			"""
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)
			f_pastn_valid = Signal(1, reset=0)
			f_pastn_counter = Signal(32, reset=0)
			m.d.sync += f_pastn_counter.eq(f_pastn_counter + 1)
			with m.If(f_pastn_counter == PERIOD - 1):
				m.d.sync += f_pastn_counter.eq(f_pastn_counter)
				m.d.sync += f_pastn_valid.eq(1)

			"""
			LED properties
			"""
			# The LED outputs are correct in each state
			with m.Switch(self.state):
				with m.Case(0):
					m.d.comb += Assert(self.leds == 0b11111111)
				with m.Case(1):
					m.d.comb += Assert(self.leds == 0b11111110)
				with m.Case(2):
					m.d.comb += Assert(self.leds == 0b11111101)
				with m.Case(3):
					m.d.comb += Assert(self.leds == 0b11111011)
				with m.Case(4):
					m.d.comb += Assert(self.leds == 0b11110111)
				with m.Case(5):
					m.d.comb += Assert(self.leds == 0b11101111)
				with m.Case(6):
					m.d.comb += Assert(self.leds == 0b11011111)
				with m.Case(7):
					m.d.comb += Assert(self.leds == 0b10111111)
				with m.Case(8):
					m.d.comb += Assert(self.leds == 0b01111111)
				with m.Case(9):
					m.d.comb += Assert(self.leds == 0b10111111)
				with m.Case(10):
					m.d.comb += Assert(self.leds == 0b11011111)
				with m.Case(11):
					m.d.comb += Assert(self.leds == 0b11101111)
				with m.Case(12):
					m.d.comb += Assert(self.leds == 0b11110111)
				with m.Case(13):
					m.d.comb += Assert(self.leds == 0b11111011)
				with m.Case(14):
					m.d.comb += Assert(self.leds == 0b11111101)
				with m.Case(15):
					m.d.comb += Assert(self.leds == 0b11111110)

			"""
			Counter properties
			"""
			# Counter never exceeds the given period
			m.d.comb += Assert(self.counter < PERIOD)

			# In the READY state, the counter is always zero
			with m.If(self.state == 0):
				m.d.comb += Assert(self.counter == 0)

			# At the beginning of every walk, the counter starts out at zero
			with m.If(f_past_valid & (Past(self.state) == 0) & (self.state == 1)):
				m.d.comb += Assert(self.counter == 0)

			# During a walk, counter always increments by 1, modulo PERIOD
			with m.If(f_past_valid & (Past(self.state) != 0)):
				m.d.comb += Assert(self.counter == (Past(self.counter) + 1) % PERIOD)

			"""
			Properties of busy signal
			"""
			# Busy is asserted precisely when a walk is being performed
			m.d.comb += Assert(self.o_busy == (self.state != 0))

			"""
			Assertions involving state and state transitions
			"""
			# The circuit is always in a valid state
			m.d.comb += Assert(self.state < 16)

			# In the READY state, the circuit responds to a request with a walk
			with m.If(f_past_valid & (Past(self.state) == 0) & Past(self.i_req)):
				m.d.comb += Assert(self.state == 1)

			# Except for the READY state, the circuit stays in each state for exactly
			# PERIOD clock cycles, and the state transitions are correct
			for i in range(1, PERIOD + 1):
				with m.If(f_pastn_valid & (Past(self.state, i) != 0) & \
					(Past(self.counter, i) == (PERIOD - i))):
					m.d.comb += Assert(Past(self.state) == Past(self.state, i))
					m.d.comb += Assert(self.state == ((Past(self.state, i) + 1) % 16))

		return m

class VersaECP5Platform(LatticeECP5Platform):
	device      = "LFE5UM-45F"
	package     = "BG381"
	speed       = "8"
	default_clk = "clk100"
	default_rst = "rst"
	resources   = [
		Resource("rst", 0, PinsN("T1", dir="i"), Attrs(IO_TYPE="LVCMOS33")),
		Resource("clk100", 0, DiffPairs("P3", "P4", dir="i"), Clock(100e6), Attrs(IO_TYPE="LVDS")),
		Resource("pclk", 0, DiffPairs("A4", "A5", dir="i"), Attrs(IO_TYPE="LVDS")),

		*LEDResources(pins="E16 D17 D18 E18 F17 F18 E17 F16", attrs=Attrs(IO_TYPE="LVCMOS25")),

		Resource("alnum_led", 0,
			Subsignal("a", PinsN("M20", dir="o")),
			Subsignal("b", PinsN("L18", dir="o")),
			Subsignal("c", PinsN("M19", dir="o")),
			Subsignal("d", PinsN("L16", dir="o")),
			Subsignal("e", PinsN("L17", dir="o")),
			Subsignal("f", PinsN("M18", dir="o")),
			Subsignal("g", PinsN("N16", dir="o")),
			Subsignal("h", PinsN("M17", dir="o")),
			Subsignal("j", PinsN("N18", dir="o")),
			Subsignal("k", PinsN("P17", dir="o")),
			Subsignal("l", PinsN("N17", dir="o")),
			Subsignal("m", PinsN("P16", dir="o")),
			Subsignal("n", PinsN("R16", dir="o")),
			Subsignal("p", PinsN("R17", dir="o")),
			Subsignal("dp", PinsN("U1", dir="o")),
			Attrs(IO_TYPE="LVCMOS25")),
		
		*SwitchResources(pins={0: "H2",  1: "K3",  2: "G3",  3: "F2" }, attrs=Attrs(IO_TYPE="LVCMOS15")),
		*SwitchResources(pins={4: "J18", 5: "K18", 6: "K19", 7: "K20"}, attrs=Attrs(IO_TYPE="LVCMOS25")),

		UARTResource(0,
			rx="C11", tx="A11",
			attrs=Attrs(IO_TYPE="LVCMOS33", PULLMODE="UP")
		),

		*SPIFlashResources(0,
			cs="R2", clk="U3", miso="W2", mosi="V2", wp="Y2", hold="W1",
			attrs=Attrs(IO_STANDARD="LVCMOS33")
		),

		Resource("eth_clk125",     0, Pins("L19", dir="i"), Clock(125e6), Attrs(IO_TYPE="LVCMOS25")),
		Resource("eth_clk125_pll", 0, Pins("U16", dir="i"), Clock(125e6), Attrs(IO_TYPE="LVCMOS25")), # NC by default
		Resource("eth_rgmii", 0,
			Subsignal("rst",     PinsN("U17", dir="o")),
			Subsignal("mdc",     Pins("T18", dir="o")),
			Subsignal("mdio",    Pins("U18", dir="io")),
			Subsignal("tx_clk",  Pins("P19", dir="o")),
			Subsignal("tx_ctl",  Pins("R20", dir="o")),
			Subsignal("tx_data", Pins("N19 N20 P18 P20", dir="o")),
			Subsignal("rx_clk",  Pins("L20", dir="i")),
			Subsignal("rx_ctl",  Pins("U19", dir="i")),
			Subsignal("rx_data", Pins("T20 U20 T19 R18", dir="i")),
			Attrs(IO_TYPE="LVCMOS25")
		),
		Resource("eth_sgmii", 0,
			Subsignal("rst",     PinsN("U17", dir="o"), Attrs(IO_TYPE="LVCMOS25")),
			Subsignal("mdc",     Pins("T18", dir="o"), Attrs(IO_TYPE="LVCMOS25")),
			Subsignal("mdio",    Pins("U18", dir="io"), Attrs(IO_TYPE="LVCMOS25")),
			Subsignal("tx",      DiffPairs("W13", "W14", dir="o")),
			Subsignal("rx",      DiffPairs("Y14", "Y15", dir="i")),
		),

		Resource("eth_clk125",     1, Pins("J20", dir="i"), Clock(125e6), Attrs(IO_TYPE="LVCMOS25")),
		Resource("eth_clk125_pll", 1, Pins("C18", dir="i"), Clock(125e6), Attrs(IO_TYPE="LVCMOS25")), # NC by default
		Resource("eth_rgmii", 1,
			Subsignal("rst",     PinsN("F20", dir="o")),
			Subsignal("mdc",     Pins("G19", dir="o")),
			Subsignal("mdio",    Pins("H20", dir="io")),
			Subsignal("tx_clk",  Pins("C20", dir="o")),
			Subsignal("tx_ctrl", Pins("E19", dir="o")),
			Subsignal("tx_data", Pins("J17 J16 D19 D20", dir="o")),
			Subsignal("rx_clk",  Pins("J19", dir="i")),
			Subsignal("rx_ctrl", Pins("F19", dir="i")),
			Subsignal("rx_data", Pins("G18 G16 H18 H17", dir="i")),
			Attrs(IO_TYPE="LVCMOS25")
		),
		Resource("eth_sgmii", 1,
			Subsignal("rst",     PinsN("F20", dir="o"), Attrs(IO_TYPE="LVCMOS25")),
			Subsignal("mdc",     Pins("G19", dir="o"), Attrs(IO_TYPE="LVCMOS25")),
			Subsignal("mdio",    Pins("H20", dir="io"), Attrs(IO_TYPE="LVCMOS25")),
			Subsignal("tx",      DiffPairs("W17", "W18", dir="o")),
			Subsignal("rx",      DiffPairs("Y16", "Y17", dir="i")),
		),

		Resource("ddr3", 0,
			Subsignal("rst",     PinsN("N4", dir="o")),
			Subsignal("clk",     DiffPairs("M4", "N5", dir="o"), Attrs(IO_TYPE="LVDS")),
			Subsignal("clk_en",  Pins("N2", dir="o")),
			Subsignal("cs",      PinsN("K1", dir="o")),
			Subsignal("we",      PinsN("M1", dir="o")),
			Subsignal("ras",     PinsN("P1", dir="o")),
			Subsignal("cas",     PinsN("L1", dir="o")),
			Subsignal("a",       Pins("P2 C4 E5 F5 B3 F4 B5 E4 C5 E3 D5 B4 C3", dir="o")),
			Subsignal("ba",      Pins("P5 N3 M3", dir="o")),
			Subsignal("dqs",     DiffPairs("K2 H4", "J1 G5", dir="io"), Attrs(IO_TYPE="LVDS")),
			Subsignal("dq",      Pins("L5 F1 K4 G1 L4 H1 G2 J3 D1 C1 E2 C2 F3 A2 E1 B1", dir="io")),
			Subsignal("dm",      Pins("J4 H5", dir="o")),
			Subsignal("odt",     Pins("L2", dir="o")),
			Attrs(IO_TYPE="LVCMOS15")
		)
	]
	connectors = [
		Connector("expcon", 1, """
		-   -   -   B19 B12 B9  E6  D6  E7  D7  B11 B6  E9  D9  B8  C8  D8  E8  C7  C6
		-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
		"""), # X3
		Connector("expcon", 2, """
		A8  -   A12 A13 B13 C13 D13 E13 A14 C14 D14 E14 D11 C10 A9  B10 D12 E12 -   -
		B15 -   C15 -   D15 -   E15 A16 B16 -   C16 D16 B17 -   C17 A17 B18 A7  A18 -
		"""), # X4
	]

	@property
	def file_templates(self):
		return {
			**super().file_templates,
			"{{name}}-openocd.cfg": r"""
			interface ftdi
			{# FTDI descriptors is identical between non-5G and 5G recent Versa boards #}
			ftdi_vid_pid 0x0403 0x6010
			ftdi_channel 0
			ftdi_layout_init 0xfff8 0xfffb
			reset_config none
			adapter_khz 25000
			# ispCLOCK device (unusable with openocd and must be bypassed)
			#jtag newtap ispclock tap -irlen 8 -expected-id 0x00191043
			# ECP5 device
			{% if "5G" in platform.device -%}
			jtag newtap ecp5 tap -irlen 8 -expected-id 0x81112043 ; # LFE5UM5G-45F
			{% else -%}
			jtag newtap ecp5 tap -irlen 8 -expected-id 0x01112043 ; # LFE5UM-45F
			{% endif %}
			"""
		}

	def toolchain_program(self, products, name):
		openocd = os.environ.get("OPENOCD", "openocd")
		with products.extract("{}-openocd.cfg".format(name), "{}.svf".format(name)) \
			as (config_filename, vector_filename):
			subprocess.check_call([openocd,
				"-f", config_filename,
				"-c", "transport select jtag; init; svf -quiet {}; exit".format(vector_filename)
			])

if __name__ == "__main__":
	"""
	Simulation
	"""
	m = Module()
	m.submodules.reqwalker = reqwalker = ReqWalker()

	sim = Simulator(m)

	def process():
		for i in range(3):
			yield reqwalker.i_req.eq(1)
			yield
			yield reqwalker.i_req.eq(0)
			for j in range(100):
				yield
		yield reqwalker.i_req.eq(1)
		for i in range(300):
			yield

	sim.add_clock(0.25)
	sim.add_sync_process(process)

	with sim.write_vcd('reqwalker.vcd', 'reqwalker.gtkw', traces=reqwalker.ports()):
		sim.run()

	"""
	Formal Verification
	"""
	class ReqWalkerTest(FHDLTestCase):
		def test_reqwalker(self):
			reqwalker = ReqWalker(fv_mode = True)
			self.assertFormal(reqwalker, mode = "prove", depth = 5)
	ReqWalkerTest().test_reqwalker()

	"""
	Build
	"""
	VersaECP5Platform().build(ReqWalker(), do_program=True)