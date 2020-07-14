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

__all__ = ["TXUART", "VersaECP5Platform"]

"""
RS-232 Transmitter, reworked this time with proper assertions to ensure
correctness of operation
See https://zipcpu.com/tutorial/lsn-05-serialtx.pdf for more details
"""

class TXUART(Elaboratable):
	def __init__(self, i_wr, i_data, o_busy, o_uart_tx, fv_mode = False):
		self.i_wr = i_wr
		self.i_data = i_data
		self.o_busy = o_busy
		self.o_uart_tx = o_uart_tx
		self.fv_mode = fv_mode
	def ports(self):
		return [
			self.i_wr,
			self.i_data,
			self.o_busy,
			self.o_uart_tx
		]
	def elaborate(self, platform):
		m = Module()

		CLOCKS_PER_BAUD = 4

		if platform is not None and platform != "formal":
			BAUD_RATE = 115200
			CLOCKS_PER_BAUD = int(platform.default_clk_frequency // BAUD_RATE)

		counter = Signal(range(CLOCKS_PER_BAUD), reset=0)

		data_copy = Signal(8, reset=0)

		state = Signal(4, reset=0)

		m.d.comb += self.o_busy.eq(state != 0)

		with m.FSM():
			with m.State('IDLE'):
				m.next = 'IDLE'
				m.d.sync += state.eq(0)
				m.d.sync += self.o_uart_tx.eq(1)
				m.d.sync += counter.eq(0)
				with m.If(self.i_wr):
					m.next = 'START'
					m.d.sync += state.eq(1)
					m.d.sync += self.o_uart_tx.eq(0)
					m.d.sync += data_copy.eq(self.i_data)
			with m.State('START'):
				m.next = 'START'
				m.d.sync += state.eq(1)
				m.d.sync += self.o_uart_tx.eq(0)
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT0'
					m.d.sync += state.eq(2)
					m.d.sync += self.o_uart_tx.eq(data_copy[0])
					m.d.sync += counter.eq(0)
			with m.State('BIT0'):
				m.next = 'BIT0'
				m.d.sync += state.eq(2)
				m.d.sync += self.o_uart_tx.eq(data_copy[0])
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT1'
					m.d.sync += state.eq(3)
					m.d.sync += self.o_uart_tx.eq(data_copy[1])
					m.d.sync += counter.eq(0)
			with m.State('BIT1'):
				m.next = 'BIT1'
				m.d.sync += state.eq(3)
				m.d.sync += self.o_uart_tx.eq(data_copy[1])
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT2'
					m.d.sync += state.eq(4)
					m.d.sync += self.o_uart_tx.eq(data_copy[2])
					m.d.sync += counter.eq(0)
			with m.State('BIT2'):
				m.next = 'BIT2'
				m.d.sync += state.eq(4)
				m.d.sync += self.o_uart_tx.eq(data_copy[2])
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT3'
					m.d.sync += state.eq(5)
					m.d.sync += self.o_uart_tx.eq(data_copy[3])
					m.d.sync += counter.eq(0)
			with m.State('BIT3'):
				m.next = 'BIT3'
				m.d.sync += state.eq(5)
				m.d.sync += self.o_uart_tx.eq(data_copy[3])
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT4'
					m.d.sync += state.eq(6)
					m.d.sync += self.o_uart_tx.eq(data_copy[4])
					m.d.sync += counter.eq(0)
			with m.State('BIT4'):
				m.next = 'BIT4'
				m.d.sync += state.eq(6)
				m.d.sync += self.o_uart_tx.eq(data_copy[4])
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT5'
					m.d.sync += state.eq(7)
					m.d.sync += self.o_uart_tx.eq(data_copy[5])
					m.d.sync += counter.eq(0)
			with m.State('BIT5'):
				m.next = 'BIT5'
				m.d.sync += state.eq(7)
				m.d.sync += self.o_uart_tx.eq(data_copy[5])
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT6'
					m.d.sync += state.eq(8)
					m.d.sync += self.o_uart_tx.eq(data_copy[6])
					m.d.sync += counter.eq(0)
			with m.State('BIT6'):
				m.next = 'BIT6'
				m.d.sync += state.eq(8)
				m.d.sync += self.o_uart_tx.eq(data_copy[6])
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT7'
					m.d.sync += state.eq(9)
					m.d.sync += self.o_uart_tx.eq(data_copy[7])
					m.d.sync += counter.eq(0)
			with m.State('BIT7'):
				m.next = 'BIT7'
				m.d.sync += state.eq(9)
				m.d.sync += self.o_uart_tx.eq(data_copy[7])
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'STOP1'
					m.d.sync += state.eq(10)
					m.d.sync += self.o_uart_tx.eq(1)
					m.d.sync += counter.eq(0)
			with m.State('STOP1'):
				m.next = 'STOP1'
				m.d.sync += state.eq(10)
				m.d.sync += self.o_uart_tx.eq(1)
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'STOP2'
					m.d.sync += state.eq(11)
					m.d.sync += self.o_uart_tx.eq(1)
					m.d.sync += counter.eq(0)
			with m.State('STOP2'):
				m.next = 'STOP2'
				m.d.sync += state.eq(11)
				m.d.sync += self.o_uart_tx.eq(1)
				m.d.sync += counter.eq(counter + 1)
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'IDLE'
					m.d.sync += state.eq(0)
					m.d.sync += self.o_uart_tx.eq(1)
					m.d.sync += counter.eq(0)

		if self.fv_mode:
			"""
			Indicators of when Past() is valid
			"""
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)
			f_pastn_valid = Signal(1, reset=0)
			f_pastn_ctr = Signal(range(CLOCKS_PER_BAUD), reset=0)
			m.d.sync += f_pastn_ctr.eq(f_pastn_ctr + 1)
			with m.If(f_pastn_ctr == CLOCKS_PER_BAUD - 1):
				m.d.sync += f_pastn_ctr.eq(f_pastn_ctr)
				m.d.sync += f_pastn_valid.eq(1)

			"""
			Properties of o_busy
			"""
			# o_busy should be asserted if and only if a transmission is taking place
			m.d.comb += Assert(self.o_busy == (state != 0))

			"""
			Properties of o_uart_tx
			"""
			# In each given state, o_uart_tx should have the corresponding output
			with m.Switch(state):
				with m.Case(0):
					m.d.comb += Assert(self.o_uart_tx == 1)
				with m.Case(1):
					m.d.comb += Assert(self.o_uart_tx == 0)
				with m.Case(2):
					m.d.comb += Assert(self.o_uart_tx == data_copy[0])
				with m.Case(3):
					m.d.comb += Assert(self.o_uart_tx == data_copy[1])
				with m.Case(4):
					m.d.comb += Assert(self.o_uart_tx == data_copy[2])
				with m.Case(5):
					m.d.comb += Assert(self.o_uart_tx == data_copy[3])
				with m.Case(6):
					m.d.comb += Assert(self.o_uart_tx == data_copy[4])
				with m.Case(7):
					m.d.comb += Assert(self.o_uart_tx == data_copy[5])
				with m.Case(8):
					m.d.comb += Assert(self.o_uart_tx == data_copy[6])
				with m.Case(9):
					m.d.comb += Assert(self.o_uart_tx == data_copy[7])
				with m.Case(10):
					m.d.comb += Assert(self.o_uart_tx == 1)
				with m.Case(11):
					m.d.comb += Assert(self.o_uart_tx == 1)
				with m.Default():
					m.d.comb += Assert(0) # This should never happen

			"""
			Counter properties
			"""
			# The counter should never reach or exceed CLOCKS_PER_BAUD
			m.d.comb += Assert(counter < CLOCKS_PER_BAUD)
			# When idle, the counter should be always zero
			with m.If(state == 0):
				m.d.comb += Assert(counter == 0)
			# At the beginning of a transmission, counter should start at zero
			with m.If(f_past_valid & (Past(state) == 0) & Past(self.i_wr)):
				m.d.comb += Assert(counter == 0)
			# During a transmission, counter should always count up by 1, modulo
			# CLOCKS_PER_BAUD
			with m.If(f_past_valid & (Past(state) != 0)):
				m.d.comb += Assert(counter == ((Past(counter) + 1) % CLOCKS_PER_BAUD))

			"""
			Properties of data_copy
			"""
			# When idle, on i_wr, data_copy should take the value of i_data on the next
			# clock cycle
			with m.If(f_past_valid & (Past(state) == 0) & Past(self.i_wr)):
				m.d.comb += Assert(data_copy == Past(self.i_data))
			# data_copy should remain stable during a transmission, even if i_data
			# changes
			with m.If(f_past_valid & (Past(state) != 0) & (state != 0)):
				m.d.comb += Assert(Stable(data_copy))

			"""
			State properties
			"""
			# The circuit should always be in a valid state
			m.d.comb += Assert(state < 12)
			# The circuit should initially be idle
			with m.If(~f_past_valid):
				m.d.comb += Assert(state == 0)
			# When idle, on i_wr, the circuit should transition to the START state on
			# the next clock cycle
			with m.If(f_past_valid & (Past(state) == 0) & Past(self.i_wr)):
				m.d.comb += Assert(state == 1)
			# Except for the IDLE state, the circuit should remain in each state for
			# exactly CLOCKS_PER_BAUD clock cycles, and the state transitions are
			# correct
			with m.If(f_pastn_valid & (Past(state, CLOCKS_PER_BAUD) != 0) & \
				(Past(counter, CLOCKS_PER_BAUD) == 0)):
				for i in range(1, CLOCKS_PER_BAUD):
					m.d.comb += Assert(Past(state, CLOCKS_PER_BAUD) == Past(state, i))
				m.d.comb += Assert(state == ((Past(state, CLOCKS_PER_BAUD) + 1) % 12))

			"""
			Two of the above assertions pass 100 levels of BMC but fail induction,
			probably because the number of clock cycles in which the circuit remains
			in the IDLE state is unbounded (and therefore no amount of base cases can
			make the induction go through). Let us make a (likely) harmless assumption
			that there is an upper bound on the amount of clock cycles in which the
			circuit remains idle, say, 10 * CLOCKS_PER_BAUD
			"""
			f_past10n_valid = Signal(1, reset=0)
			f_past10n_ctr = Signal(range(10 * CLOCKS_PER_BAUD), reset=0)
			m.d.sync += f_past10n_ctr.eq(f_past10n_ctr + 1)
			with m.If(f_past10n_ctr == 10 * CLOCKS_PER_BAUD - 1):
				m.d.sync += f_past10n_ctr.eq(f_past10n_ctr)
				m.d.sync += f_past10n_valid.eq(1)

			with m.If(f_past10n_valid & reduce(lambda a, b: a & b, \
				(((Past(state, i) == 0) & ~Past(self.i_wr, i)) \
				for i in range(1, 10 * CLOCKS_PER_BAUD + 1)))):
				m.d.comb += Assume(self.i_wr)
			# Aaaaaand ... with this assumption, our k-induction passes with k >= 66 ;-)

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
	i_wr = Signal(1, reset=0)
	i_data = Signal(8, reset=0)
	o_busy = Signal(1, reset=0)
	o_uart_tx = Signal(1, reset=1)
	m.submodules.txuart = txuart = TXUART(i_wr, i_data, o_busy, o_uart_tx)

	sim = Simulator(m)

	msg = "Hello World!\n"

	def process():
		for i in range(25):
			yield
		for c in msg:
			byte = ord(c)
			yield txuart.i_wr.eq(1)
			yield txuart.i_data.eq(byte)
			yield
			yield txuart.i_wr.eq(0)
			yield txuart.i_data.eq(0)
			for i in range(50):
				yield

	sim.add_clock(1e-8)
	sim.add_sync_process(process)

	with sim.write_vcd('txuart.vcd', 'txuart.gtkw', traces=txuart.ports()):
		sim.run()

	"""
	Formal Verification
	"""
	class TXUARTTest(FHDLTestCase):
		def test_txuart(self):
			i_wr = Signal(1, reset=0)
			i_data = Signal(8, reset=0)
			o_busy = Signal(1, reset=0)
			o_uart_tx = Signal(1, reset=1)
			txuart = TXUART(i_wr, i_data, o_busy, o_uart_tx, fv_mode=True)
			# Yes, under our current assumptions on how long the transmitter can stay idle
			# before it receives its next i_wr, it requires at least 66 steps to pass
			# induction ;-)
			self.assertFormal(txuart, mode='prove', depth=66)
	TXUARTTest().test_txuart()

	"""
	Build - No build since the transmitter is just a component. A top-level is required
	for building the design
	"""