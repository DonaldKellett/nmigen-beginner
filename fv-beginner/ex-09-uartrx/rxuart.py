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

from f_txuart import *

__all__ = ['RXUART', 'VersaECP5Platform']

"""
RS-232 receiver, this time formally verified with appropriate assertions
See http://zipcpu.com/tutorial/lsn-09-serialrx.pdf for more details
"""

class RXUART(Elaboratable):
	def __init__(self, i_uart_rx, o_stb, o_data, fv_mode=False):
		self.i_uart_rx = i_uart_rx
		self.o_stb = o_stb
		self.o_data = o_data
		self.fv_mode = fv_mode
	def ports(self):
		return [self.i_uart_rx, self.o_stb, self.o_data]
	def elaborate(self, platform):
		m = Module()

		CLOCKS_PER_BAUD = 4

		if platform is not None and platform != "formal":
			BAUD_RATE = 115200
			CLOCKS_PER_BAUD = int(platform.default_clk_frequency // BAUD_RATE)
			self.i_uart_rx = platform.request('uart').rx.i
			m.d.comb += Cat(*(platform.request('led', i).o for i in range(8))).eq(~self.o_data)

		counter = Signal(range(CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2)), reset=0)

		# 2FF-synchronizer for dealing with metastability
		# So we should use ck_uart for the stabilized receiver input instead of the original
		# i_uart_rx
		# Consequence: The data we read in is two clock cycles late, which we'll need to account
		# for in our formal properties
		ck_uart = Signal(1, reset=1)
		q_uart = Signal(1, reset=1)
		m.d.sync += Cat(q_uart, ck_uart).eq(Cat(self.i_uart_rx, q_uart))

		state = Signal(4, reset=0)

		m.d.sync += self.o_stb.eq(0)
		m.d.sync += counter.eq(counter + 1)
		with m.FSM():
			with m.State('READY'):
				m.next = 'READY'
				m.d.sync += counter.eq(0)
				with m.If(ck_uart == 0):
					m.next = 'BIT0'
					m.d.sync += state.eq(1)
					m.d.sync += counter.eq(1)
			with m.State('BIT0'):
				m.next = 'BIT0'
				with m.If(counter == CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) - 1):
					m.next = 'BIT1'
					m.d.sync += self.o_data[0].eq(ck_uart)
					m.d.sync += counter.eq(0)
					m.d.sync += state.eq(2)
			with m.State('BIT1'):
				m.next = 'BIT1'
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT2'
					m.d.sync += self.o_data[1].eq(ck_uart)
					m.d.sync += counter.eq(0)
					m.d.sync += state.eq(3)
			with m.State('BIT2'):
				m.next = 'BIT2'
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT3'
					m.d.sync += self.o_data[2].eq(ck_uart)
					m.d.sync += counter.eq(0)
					m.d.sync += state.eq(4)
			with m.State('BIT3'):
				m.next = 'BIT3'
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT4'
					m.d.sync += self.o_data[3].eq(ck_uart)
					m.d.sync += counter.eq(0)
					m.d.sync += state.eq(5)
			with m.State('BIT4'):
				m.next = 'BIT4'
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT5'
					m.d.sync += self.o_data[4].eq(ck_uart)
					m.d.sync += counter.eq(0)
					m.d.sync += state.eq(6)
			with m.State('BIT5'):
				m.next = 'BIT5'
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT6'
					m.d.sync += self.o_data[5].eq(ck_uart)
					m.d.sync += counter.eq(0)
					m.d.sync += state.eq(7)
			with m.State('BIT6'):
				m.next = 'BIT6'
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'BIT7'
					m.d.sync += self.o_data[6].eq(ck_uart)
					m.d.sync += counter.eq(0)
					m.d.sync += state.eq(8)
			with m.State('BIT7'):
				m.next = 'BIT7'
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'STOP'
					m.d.sync += self.o_data[7].eq(ck_uart)
					m.d.sync += counter.eq(0)
					m.d.sync += state.eq(9)
			with m.State('STOP'):
				m.next = 'STOP'
				with m.If(counter == CLOCKS_PER_BAUD - 1):
					m.next = 'READY'
					m.d.sync += self.o_stb.eq(ck_uart)
					m.d.sync += counter.eq(0)
					m.d.sync += state.eq(0)

		if self.fv_mode:
			i_wr = Signal(1, reset=0)
			i_data = Signal(8, reset=0)
			o_busy = Signal(1, reset=0)
			o_uart_tx = self.i_uart_rx
			m.submodules.f_txuart = f_txuart = FTXUART(i_wr, i_data, o_busy, o_uart_tx, fv_mode=True)

			"""
			Indicator of when Past() is valid
			"""
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			"""
			Properties of o_stb
			"""
			# o_stb is asserted precisely for one clock cycle after it encounters a valid stop bit and
			# is de-asserted otherwise
			with m.If(f_past_valid & (Past(state) == 9) & (Past(counter) == CLOCKS_PER_BAUD - 1) & \
				Past(ck_uart)):
				m.d.comb += Assert(self.o_stb)
			with m.Else():
				m.d.comb += Assert(~self.o_stb)

			"""
			Properties of o_data
			"""
			# In state BIT1, o_data[:1] matches f_data[:1]
			with m.If(state == 2):
				m.d.comb += Assert(self.o_data[:1] == f_txuart.f_data[:1])
			# In state BIT2, o_data[:2] matches f_data[:2]
			with m.If(state == 3):
				m.d.comb += Assert(self.o_data[:2] == f_txuart.f_data[:2])
			# In state BIT3, o_data[:3] matches f_data[:3]
			with m.If(state == 4):
				m.d.comb += Assert(self.o_data[:3] == f_txuart.f_data[:3])
			# In state BIT4, o_data[:4] matches f_data[:4]
			with m.If(state == 5):
				m.d.comb += Assert(self.o_data[:4] == f_txuart.f_data[:4])
			# In state BIT5, o_data[:5] matches f_data[:5]
			with m.If(state == 6):
				m.d.comb += Assert(self.o_data[:5] == f_txuart.f_data[:5])
			# In state BIT6, o_data[:6] matches f_data[:6]
			with m.If(state == 7):
				m.d.comb += Assert(self.o_data[:6] == f_txuart.f_data[:6])
			# In state BIT7, o_data[:7] matches f_data[:7]
			with m.If(state == 8):
				m.d.comb += Assert(self.o_data[:7] == f_txuart.f_data[:7])
			# In state STOP, o_data[:8] matches f_data[:8]
			with m.If(state == 9):
				m.d.comb += Assert(self.o_data[:8] == f_txuart.f_data[:8])
			# Therefore, whenever o_stb is asserted, o_data matches f_data exactly (thus the receiver
			# received the correct byte)
			with m.If(self.o_stb):
				m.d.comb += Assert(self.o_data == f_txuart.f_data)

			"""
			Properties of counter
			"""
			# When in the ready state, counter is always zero
			with m.If(state == 0):
				m.d.comb += Assert(counter == 0)
			# In state BIT0, counter + 2 == f_counter
			with m.If(state == 1):
				m.d.comb += Assert(counter + 2 == f_txuart.f_counter)
			# In state BIT1, counter + 2 + CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == f_counter
			with m.If(state == 2):
				m.d.comb += Assert(counter + 2 + CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == \
					f_txuart.f_counter)
			# In state BIT2, counter + 2 + 2 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == f_counter
			with m.If(state == 3):
				m.d.comb += Assert(counter + 2 + 2 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == \
					f_txuart.f_counter)
			# In state BIT3, counter + 2 + 3 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == f_counter
			with m.If(state == 4):
				m.d.comb += Assert(counter + 2 + 3 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == \
					f_txuart.f_counter)
			# In state BIT4, counter + 2 + 4 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == f_counter
			with m.If(state == 5):
				m.d.comb += Assert(counter + 2 + 4 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == \
					f_txuart.f_counter)
			# In state BIT5, counter + 2 + 5 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == f_counter
			with m.If(state == 6):
				m.d.comb += Assert(counter + 2 + 5 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == \
					f_txuart.f_counter)
			# In state BIT6, counter + 2 + 6 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == f_counter
			with m.If(state == 7):
				m.d.comb += Assert(counter + 2 + 6 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == \
					f_txuart.f_counter)
			# In state BIT7, counter + 2 + 7 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == f_counter
			with m.If(state == 8):
				m.d.comb += Assert(counter + 2 + 7 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == \
					f_txuart.f_counter)
			# In state STOP, counter + 2 + 8 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == f_counter
			with m.If(state == 9):
				m.d.comb += Assert(counter + 2 + 8 * CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) == \
					f_txuart.f_counter)

			"""
			Properties of ck_uart
			"""
			# ck_uart is asserted for the first two clock cycles, and is two clock cycles behind
			# i_uart_rx otherwise
			f_past2_valid = Signal(1, reset=0)
			with m.If(f_past_valid):
				m.d.sync += f_past2_valid.eq(1)
			with m.If(~f_past2_valid):
				m.d.comb += Assert(ck_uart)
			with m.Else():
				m.d.comb += Assert(ck_uart == Past(self.i_uart_rx, 2))

			"""
			Properties of q_uart
			"""
			# q_uart is asserted for the first clock cycle, and is one clock cycle behind
			# i_uart_rx otherwise
			with m.If(~f_past_valid):
				m.d.comb += Assert(q_uart)
			with m.Else():
				m.d.comb += Assert(q_uart == Past(self.i_uart_rx))

			"""
			Properties of state
			"""
			# Initial state is READY
			with m.If(~f_past_valid):
				m.d.comb += Assert(state == 0)
			# The receiver never enters an invalid state
			m.d.comb += Assert(state < 10)
			# In the READY state, a start bit (i.e. ck_uart going low) triggers the state transition to
			# BIT0, and nothing else can trigger a state transition
			with m.If(f_past_valid & (Past(state) == 0)):
				with m.If(Past(ck_uart) == 0):
					m.d.comb += Assert(state == 1)
				with m.Else():
					m.d.comb += Assert(Stable(state))
			# In the BIT0 state, a state transition to BIT1 is triggered if and only if counter reaches
			# CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) - 1
			with m.If(f_past_valid & (Past(state) == 1)):
				with m.If(Past(counter) == CLOCKS_PER_BAUD + int(CLOCKS_PER_BAUD // 2) - 1):
					m.d.comb += Assert(state == 2)
				with m.Else():
					m.d.comb += Assert(Stable(state))
			# In every other state, a state transition is triggered if and only if counter reaches
			# CLOCKS_PER_BAUD - 1, and the state transitions are correct
			with m.If(f_past_valid & (Past(state) >= 2)):
				with m.If(Past(counter) == CLOCKS_PER_BAUD - 1):
					m.d.comb += Assert(state == (Past(state) + 1) % 10)
				with m.Else():
					m.d.comb += Assert(Stable(state))

		return m

if __name__ == '__main__':
	"""
	Simulation
	"""
	m = Module()
	i_wr = Signal(1, reset=0)
	i_data = Signal(8, reset=0)
	o_busy = Signal(1, reset=0)
	o_uart_tx = Signal(1, reset=1)
	m.submodules.f_txuart = f_txuart = FTXUART(i_wr, i_data, o_busy, o_uart_tx)
	i_uart_rx = o_uart_tx
	o_stb = Signal(1, reset=0)
	o_data = Signal(8, reset=0)
	m.submodules.rxuart = rxuart = RXUART(i_uart_rx, o_stb, o_data)

	sim = Simulator(m)

	def process():
		tx_msg = "Hello World!"
		rx_msg = ""
		for c in tx_msg:
			yield i_data.eq(ord(c))
			yield i_wr.eq(1)
			yield
			yield i_data.eq(0)
			yield i_wr.eq(0)
			while (yield o_stb) == 0:
				yield
			rx_msg += chr((yield o_data))
			while (yield o_busy) == 1:
				yield
		print(rx_msg) # Should be the same as tx_msg

	sim.add_clock(1e-8)
	sim.add_sync_process(process)
	with sim.write_vcd('rxuart.vcd', 'rxuart.gtkw', traces=rxuart.ports()):
		sim.run()

	"""
	Formal Verification
	"""
	class RXUARTTest(FHDLTestCase):
		def test_rxuart(self):
			i_uart_rx = Signal(1, reset=1)
			o_stb = Signal(1, reset=0)
			o_data = Signal(8, reset=0)
			self.assertFormal(RXUART(i_uart_rx, o_stb, o_data, fv_mode=True), mode='prove', depth=41)
	RXUARTTest().test_rxuart()

	"""
	Build
	"""
	i_uart_rx = Signal(1, reset=1)
	o_stb = Signal(1, reset=0)
	o_data = Signal(8, reset=0)
	VersaECP5Platform().build(RXUART(i_uart_rx, o_stb, o_data), do_program=True)