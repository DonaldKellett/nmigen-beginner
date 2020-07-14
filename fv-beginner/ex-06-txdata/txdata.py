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

from counter import *
from chgdetector import *
from txuart import *

__all__ = ['TXData', 'TXDataDemo', 'VersaECP5Platform']

class TXData(Elaboratable):
	def __init__(self, i_stb, i_data, o_busy, o_uart_tx, fv_mode=False):
		self.i_stb = i_stb
		self.i_data = i_data
		self.o_busy = o_busy
		self.o_uart_tx = o_uart_tx
		self.fv_mode = fv_mode
	def ports(self):
		return [
			self.i_stb,
			self.i_data,
			self.o_busy,
			self.o_uart_tx
		]
	def elaborate(self, platform):
		m = Module()

		o_wr = Signal(1, reset=0)
		o_data = Signal(8, reset=0)
		i_busy = Signal(1, reset=0)
		m.submodules.txuart = TXUART(o_wr, o_data, i_busy, self.o_uart_tx, self.fv_mode)

		data_copy = Signal(32, reset=0)
		state = Signal(4, reset=0)
		counter = Signal(32, reset=0)

		m.d.comb += self.o_busy.eq(state != 0)
		m.d.sync += counter.eq(counter + 1)

		with m.FSM():
			with m.State('IDLE'):
				m.next = 'IDLE'
				m.d.sync += counter.eq(0)
				with m.If(self.i_stb):
					m.next = 'ZERO'
					m.d.sync += state.eq(1)
					m.d.sync += o_wr.eq(1)
					m.d.sync += o_data.eq(ord('0'))
					m.d.sync += data_copy.eq(self.i_data)
			with m.State('ZERO'):
				m.next = 'ZERO'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'X'
					m.d.sync += state.eq(2)
					m.d.sync += o_wr.eq(1)
					m.d.sync += o_data.eq(ord('x'))
					m.d.sync += counter.eq(0)
			with m.State('X'):
				m.next = 'X'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'HEX7'
					m.d.sync += state.eq(3)
					m.d.sync += o_wr.eq(1)
					with m.Switch(data_copy[28:]):
						with m.Case(0x0):
							m.d.sync += o_data.eq(ord('0'))
						with m.Case(0x1):
							m.d.sync += o_data.eq(ord('1'))
						with m.Case(0x2):
							m.d.sync += o_data.eq(ord('2'))
						with m.Case(0x3):
							m.d.sync += o_data.eq(ord('3'))
						with m.Case(0x4):
							m.d.sync += o_data.eq(ord('4'))
						with m.Case(0x5):
							m.d.sync += o_data.eq(ord('5'))
						with m.Case(0x6):
							m.d.sync += o_data.eq(ord('6'))
						with m.Case(0x7):
							m.d.sync += o_data.eq(ord('7'))
						with m.Case(0x8):
							m.d.sync += o_data.eq(ord('8'))
						with m.Case(0x9):
							m.d.sync += o_data.eq(ord('9'))
						with m.Case(0xa):
							m.d.sync += o_data.eq(ord('a'))
						with m.Case(0xb):
							m.d.sync += o_data.eq(ord('b'))
						with m.Case(0xc):
							m.d.sync += o_data.eq(ord('c'))
						with m.Case(0xd):
							m.d.sync += o_data.eq(ord('d'))
						with m.Case(0xe):
							m.d.sync += o_data.eq(ord('e'))
						with m.Case(0xf):
							m.d.sync += o_data.eq(ord('f'))
					m.d.sync += counter.eq(0)
			with m.State('HEX7'):
				m.next = 'HEX7'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'HEX6'
					m.d.sync += state.eq(4)
					m.d.sync += o_wr.eq(1)
					with m.Switch(data_copy[24:28]):
						with m.Case(0x0):
							m.d.sync += o_data.eq(ord('0'))
						with m.Case(0x1):
							m.d.sync += o_data.eq(ord('1'))
						with m.Case(0x2):
							m.d.sync += o_data.eq(ord('2'))
						with m.Case(0x3):
							m.d.sync += o_data.eq(ord('3'))
						with m.Case(0x4):
							m.d.sync += o_data.eq(ord('4'))
						with m.Case(0x5):
							m.d.sync += o_data.eq(ord('5'))
						with m.Case(0x6):
							m.d.sync += o_data.eq(ord('6'))
						with m.Case(0x7):
							m.d.sync += o_data.eq(ord('7'))
						with m.Case(0x8):
							m.d.sync += o_data.eq(ord('8'))
						with m.Case(0x9):
							m.d.sync += o_data.eq(ord('9'))
						with m.Case(0xa):
							m.d.sync += o_data.eq(ord('a'))
						with m.Case(0xb):
							m.d.sync += o_data.eq(ord('b'))
						with m.Case(0xc):
							m.d.sync += o_data.eq(ord('c'))
						with m.Case(0xd):
							m.d.sync += o_data.eq(ord('d'))
						with m.Case(0xe):
							m.d.sync += o_data.eq(ord('e'))
						with m.Case(0xf):
							m.d.sync += o_data.eq(ord('f'))
					m.d.sync += counter.eq(0)
			with m.State('HEX6'):
				m.next = 'HEX6'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'HEX5'
					m.d.sync += state.eq(5)
					m.d.sync += o_wr.eq(1)
					with m.Switch(data_copy[20:24]):
						with m.Case(0x0):
							m.d.sync += o_data.eq(ord('0'))
						with m.Case(0x1):
							m.d.sync += o_data.eq(ord('1'))
						with m.Case(0x2):
							m.d.sync += o_data.eq(ord('2'))
						with m.Case(0x3):
							m.d.sync += o_data.eq(ord('3'))
						with m.Case(0x4):
							m.d.sync += o_data.eq(ord('4'))
						with m.Case(0x5):
							m.d.sync += o_data.eq(ord('5'))
						with m.Case(0x6):
							m.d.sync += o_data.eq(ord('6'))
						with m.Case(0x7):
							m.d.sync += o_data.eq(ord('7'))
						with m.Case(0x8):
							m.d.sync += o_data.eq(ord('8'))
						with m.Case(0x9):
							m.d.sync += o_data.eq(ord('9'))
						with m.Case(0xa):
							m.d.sync += o_data.eq(ord('a'))
						with m.Case(0xb):
							m.d.sync += o_data.eq(ord('b'))
						with m.Case(0xc):
							m.d.sync += o_data.eq(ord('c'))
						with m.Case(0xd):
							m.d.sync += o_data.eq(ord('d'))
						with m.Case(0xe):
							m.d.sync += o_data.eq(ord('e'))
						with m.Case(0xf):
							m.d.sync += o_data.eq(ord('f'))
					m.d.sync += counter.eq(0)
			with m.State('HEX5'):
				m.next = 'HEX5'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'HEX4'
					m.d.sync += state.eq(6)
					m.d.sync += o_wr.eq(1)
					with m.Switch(data_copy[16:20]):
						with m.Case(0x0):
							m.d.sync += o_data.eq(ord('0'))
						with m.Case(0x1):
							m.d.sync += o_data.eq(ord('1'))
						with m.Case(0x2):
							m.d.sync += o_data.eq(ord('2'))
						with m.Case(0x3):
							m.d.sync += o_data.eq(ord('3'))
						with m.Case(0x4):
							m.d.sync += o_data.eq(ord('4'))
						with m.Case(0x5):
							m.d.sync += o_data.eq(ord('5'))
						with m.Case(0x6):
							m.d.sync += o_data.eq(ord('6'))
						with m.Case(0x7):
							m.d.sync += o_data.eq(ord('7'))
						with m.Case(0x8):
							m.d.sync += o_data.eq(ord('8'))
						with m.Case(0x9):
							m.d.sync += o_data.eq(ord('9'))
						with m.Case(0xa):
							m.d.sync += o_data.eq(ord('a'))
						with m.Case(0xb):
							m.d.sync += o_data.eq(ord('b'))
						with m.Case(0xc):
							m.d.sync += o_data.eq(ord('c'))
						with m.Case(0xd):
							m.d.sync += o_data.eq(ord('d'))
						with m.Case(0xe):
							m.d.sync += o_data.eq(ord('e'))
						with m.Case(0xf):
							m.d.sync += o_data.eq(ord('f'))
					m.d.sync += counter.eq(0)
			with m.State('HEX4'):
				m.next = 'HEX4'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'HEX3'
					m.d.sync += state.eq(7)
					m.d.sync += o_wr.eq(1)
					with m.Switch(data_copy[12:16]):
						with m.Case(0x0):
							m.d.sync += o_data.eq(ord('0'))
						with m.Case(0x1):
							m.d.sync += o_data.eq(ord('1'))
						with m.Case(0x2):
							m.d.sync += o_data.eq(ord('2'))
						with m.Case(0x3):
							m.d.sync += o_data.eq(ord('3'))
						with m.Case(0x4):
							m.d.sync += o_data.eq(ord('4'))
						with m.Case(0x5):
							m.d.sync += o_data.eq(ord('5'))
						with m.Case(0x6):
							m.d.sync += o_data.eq(ord('6'))
						with m.Case(0x7):
							m.d.sync += o_data.eq(ord('7'))
						with m.Case(0x8):
							m.d.sync += o_data.eq(ord('8'))
						with m.Case(0x9):
							m.d.sync += o_data.eq(ord('9'))
						with m.Case(0xa):
							m.d.sync += o_data.eq(ord('a'))
						with m.Case(0xb):
							m.d.sync += o_data.eq(ord('b'))
						with m.Case(0xc):
							m.d.sync += o_data.eq(ord('c'))
						with m.Case(0xd):
							m.d.sync += o_data.eq(ord('d'))
						with m.Case(0xe):
							m.d.sync += o_data.eq(ord('e'))
						with m.Case(0xf):
							m.d.sync += o_data.eq(ord('f'))
					m.d.sync += counter.eq(0)
			with m.State('HEX3'):
				m.next = 'HEX3'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'HEX2'
					m.d.sync += state.eq(8)
					m.d.sync += o_wr.eq(1)
					with m.Switch(data_copy[8:12]):
						with m.Case(0x0):
							m.d.sync += o_data.eq(ord('0'))
						with m.Case(0x1):
							m.d.sync += o_data.eq(ord('1'))
						with m.Case(0x2):
							m.d.sync += o_data.eq(ord('2'))
						with m.Case(0x3):
							m.d.sync += o_data.eq(ord('3'))
						with m.Case(0x4):
							m.d.sync += o_data.eq(ord('4'))
						with m.Case(0x5):
							m.d.sync += o_data.eq(ord('5'))
						with m.Case(0x6):
							m.d.sync += o_data.eq(ord('6'))
						with m.Case(0x7):
							m.d.sync += o_data.eq(ord('7'))
						with m.Case(0x8):
							m.d.sync += o_data.eq(ord('8'))
						with m.Case(0x9):
							m.d.sync += o_data.eq(ord('9'))
						with m.Case(0xa):
							m.d.sync += o_data.eq(ord('a'))
						with m.Case(0xb):
							m.d.sync += o_data.eq(ord('b'))
						with m.Case(0xc):
							m.d.sync += o_data.eq(ord('c'))
						with m.Case(0xd):
							m.d.sync += o_data.eq(ord('d'))
						with m.Case(0xe):
							m.d.sync += o_data.eq(ord('e'))
						with m.Case(0xf):
							m.d.sync += o_data.eq(ord('f'))
					m.d.sync += counter.eq(0)
			with m.State('HEX2'):
				m.next = 'HEX2'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'HEX1'
					m.d.sync += state.eq(9)
					m.d.sync += o_wr.eq(1)
					with m.Switch(data_copy[4:8]):
						with m.Case(0x0):
							m.d.sync += o_data.eq(ord('0'))
						with m.Case(0x1):
							m.d.sync += o_data.eq(ord('1'))
						with m.Case(0x2):
							m.d.sync += o_data.eq(ord('2'))
						with m.Case(0x3):
							m.d.sync += o_data.eq(ord('3'))
						with m.Case(0x4):
							m.d.sync += o_data.eq(ord('4'))
						with m.Case(0x5):
							m.d.sync += o_data.eq(ord('5'))
						with m.Case(0x6):
							m.d.sync += o_data.eq(ord('6'))
						with m.Case(0x7):
							m.d.sync += o_data.eq(ord('7'))
						with m.Case(0x8):
							m.d.sync += o_data.eq(ord('8'))
						with m.Case(0x9):
							m.d.sync += o_data.eq(ord('9'))
						with m.Case(0xa):
							m.d.sync += o_data.eq(ord('a'))
						with m.Case(0xb):
							m.d.sync += o_data.eq(ord('b'))
						with m.Case(0xc):
							m.d.sync += o_data.eq(ord('c'))
						with m.Case(0xd):
							m.d.sync += o_data.eq(ord('d'))
						with m.Case(0xe):
							m.d.sync += o_data.eq(ord('e'))
						with m.Case(0xf):
							m.d.sync += o_data.eq(ord('f'))
					m.d.sync += counter.eq(0)
			with m.State('HEX1'):
				m.next = 'HEX1'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'HEX0'
					m.d.sync += state.eq(10)
					m.d.sync += o_wr.eq(1)
					with m.Switch(data_copy[:4]):
						with m.Case(0x0):
							m.d.sync += o_data.eq(ord('0'))
						with m.Case(0x1):
							m.d.sync += o_data.eq(ord('1'))
						with m.Case(0x2):
							m.d.sync += o_data.eq(ord('2'))
						with m.Case(0x3):
							m.d.sync += o_data.eq(ord('3'))
						with m.Case(0x4):
							m.d.sync += o_data.eq(ord('4'))
						with m.Case(0x5):
							m.d.sync += o_data.eq(ord('5'))
						with m.Case(0x6):
							m.d.sync += o_data.eq(ord('6'))
						with m.Case(0x7):
							m.d.sync += o_data.eq(ord('7'))
						with m.Case(0x8):
							m.d.sync += o_data.eq(ord('8'))
						with m.Case(0x9):
							m.d.sync += o_data.eq(ord('9'))
						with m.Case(0xa):
							m.d.sync += o_data.eq(ord('a'))
						with m.Case(0xb):
							m.d.sync += o_data.eq(ord('b'))
						with m.Case(0xc):
							m.d.sync += o_data.eq(ord('c'))
						with m.Case(0xd):
							m.d.sync += o_data.eq(ord('d'))
						with m.Case(0xe):
							m.d.sync += o_data.eq(ord('e'))
						with m.Case(0xf):
							m.d.sync += o_data.eq(ord('f'))
					m.d.sync += counter.eq(0)
			with m.State('HEX0'):
				m.next = 'HEX0'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'NEWLINE'
					m.d.sync += state.eq(11)
					m.d.sync += o_wr.eq(1)
					m.d.sync += o_data.eq(ord('\n'))
					m.d.sync += counter.eq(0)
			with m.State('NEWLINE'):
				m.next = 'NEWLINE'
				m.d.sync += o_wr.eq(0)
				with m.If((counter != 0) & ~i_busy):
					m.next = 'IDLE'
					m.d.sync += state.eq(0)
					m.d.sync += counter.eq(0)

		if self.fv_mode:
			"""
			Indicator of when Past() is valid
			"""
			f_past_valid = Signal(1, reset=0)
			m.d.sync += f_past_valid.eq(1)

			"""
			Assumptions on input pins
			"""
			# i_stb is never asserted when o_busy is asserted
			with m.If(self.o_busy):
				m.d.comb += Assume(~self.i_stb)
			# When idle, i_stb is never de-asserted for more than 10 consecutive clock
			# cycles
			# This may be required for k-induction to pass
			f_past10_valid = Signal(1, reset=0)
			f_past10_ctr = Signal(range(10), reset=0)
			m.d.sync += f_past10_ctr.eq(f_past10_ctr + 1)
			with m.If(f_past10_ctr == 9):
				m.d.sync += f_past10_ctr.eq(f_past10_ctr)
				m.d.sync += f_past10_valid.eq(1)

			with m.If(f_past10_valid & reduce(lambda a, b: a & b, \
				(((Past(state, i) == 0) & ~Past(self.i_stb, i)) for i in range(1, 11)))):
				m.d.comb += Assume(self.i_stb)
			# i_busy is initially de-asserted
			with m.If(~f_past_valid):
				m.d.comb += Assume(~i_busy)
			# If i_busy was de-asserted and o_wr was asserted on the previous clock cycle
			# then i_busy is asserted in this clock cycle, i.e. an idle UART transmitter
			# should respond immediately to write requests
			with m.If(f_past_valid & (~Past(i_busy)) & Past(o_wr)):
				m.d.comb += Assume(i_busy)
			# The UART transmitter should not become busy on its own
			with m.If(f_past_valid & (~Past(i_busy)) & ~Past(o_wr)):
				m.d.comb += Assume(~i_busy)
			# i_busy is never asserted for more than 10 consecutive clock cycles
			# This may be required for k-induction to pass
			with m.If(f_past10_valid & reduce(lambda a, b: a & b, \
				(Past(i_busy, i) for i in range(1, 11)))):
				m.d.comb += Assume(~i_busy)

			"""
			Properties of o_busy
			"""
			# o_busy is asserted if and only if a transmission is taking place
			m.d.comb += Assert(self.o_busy == (state != 0))

			"""
			We do not state/assert any properties on o_uart_tx since that is just the
			UART transmitter output, and we have already verified our transmitter
			"""

			"""
			Properties of o_wr
			"""
			# o_wr is initially de-asserted
			with m.If(~f_past_valid):
				m.d.comb += Assert(~o_wr)
			# o_wr is never asserted when idle
			with m.If(state == 0):
				m.d.comb += Assert(~o_wr)
			# o_wr is never asserted when i_busy is asserted
			with m.If(i_busy):
				m.d.comb += Assert(~o_wr)
			# Except when idle, o_wr is asserted in the first clock cycle of every state
			# and de-asserted every other time
			with m.If(state != 0):
				m.d.comb += Assert(o_wr == (counter == 0))

			"""
			Properties of o_data
			"""
			# Except when idle (where o_data is a don't care), o_data should contain the
			# correct character in each state
			with m.Switch(state):
				with m.Case(0):
					m.d.comb += Assert(1)
				with m.Case(1):
					m.d.comb += Assert(o_data == ord('0'))
				with m.Case(2):
					m.d.comb += Assert(o_data == ord('x'))
				with m.Case(3):
					with m.Switch(data_copy[28:]):
						with m.Case(0x0):
							m.d.comb += Assert(o_data == ord('0'))
						with m.Case(0x1):
							m.d.comb += Assert(o_data == ord('1'))
						with m.Case(0x2):
							m.d.comb += Assert(o_data == ord('2'))
						with m.Case(0x3):
							m.d.comb += Assert(o_data == ord('3'))
						with m.Case(0x4):
							m.d.comb += Assert(o_data == ord('4'))
						with m.Case(0x5):
							m.d.comb += Assert(o_data == ord('5'))
						with m.Case(0x6):
							m.d.comb += Assert(o_data == ord('6'))
						with m.Case(0x7):
							m.d.comb += Assert(o_data == ord('7'))
						with m.Case(0x8):
							m.d.comb += Assert(o_data == ord('8'))
						with m.Case(0x9):
							m.d.comb += Assert(o_data == ord('9'))
						with m.Case(0xa):
							m.d.comb += Assert(o_data == ord('a'))
						with m.Case(0xb):
							m.d.comb += Assert(o_data == ord('b'))
						with m.Case(0xc):
							m.d.comb += Assert(o_data == ord('c'))
						with m.Case(0xd):
							m.d.comb += Assert(o_data == ord('d'))
						with m.Case(0xe):
							m.d.comb += Assert(o_data == ord('e'))
						with m.Case(0xf):
							m.d.comb += Assert(o_data == ord('f'))
				with m.Case(4):
					with m.Switch(data_copy[24:28]):
						with m.Case(0x0):
							m.d.comb += Assert(o_data == ord('0'))
						with m.Case(0x1):
							m.d.comb += Assert(o_data == ord('1'))
						with m.Case(0x2):
							m.d.comb += Assert(o_data == ord('2'))
						with m.Case(0x3):
							m.d.comb += Assert(o_data == ord('3'))
						with m.Case(0x4):
							m.d.comb += Assert(o_data == ord('4'))
						with m.Case(0x5):
							m.d.comb += Assert(o_data == ord('5'))
						with m.Case(0x6):
							m.d.comb += Assert(o_data == ord('6'))
						with m.Case(0x7):
							m.d.comb += Assert(o_data == ord('7'))
						with m.Case(0x8):
							m.d.comb += Assert(o_data == ord('8'))
						with m.Case(0x9):
							m.d.comb += Assert(o_data == ord('9'))
						with m.Case(0xa):
							m.d.comb += Assert(o_data == ord('a'))
						with m.Case(0xb):
							m.d.comb += Assert(o_data == ord('b'))
						with m.Case(0xc):
							m.d.comb += Assert(o_data == ord('c'))
						with m.Case(0xd):
							m.d.comb += Assert(o_data == ord('d'))
						with m.Case(0xe):
							m.d.comb += Assert(o_data == ord('e'))
						with m.Case(0xf):
							m.d.comb += Assert(o_data == ord('f'))
				with m.Case(5):
					with m.Switch(data_copy[20:24]):
						with m.Case(0x0):
							m.d.comb += Assert(o_data == ord('0'))
						with m.Case(0x1):
							m.d.comb += Assert(o_data == ord('1'))
						with m.Case(0x2):
							m.d.comb += Assert(o_data == ord('2'))
						with m.Case(0x3):
							m.d.comb += Assert(o_data == ord('3'))
						with m.Case(0x4):
							m.d.comb += Assert(o_data == ord('4'))
						with m.Case(0x5):
							m.d.comb += Assert(o_data == ord('5'))
						with m.Case(0x6):
							m.d.comb += Assert(o_data == ord('6'))
						with m.Case(0x7):
							m.d.comb += Assert(o_data == ord('7'))
						with m.Case(0x8):
							m.d.comb += Assert(o_data == ord('8'))
						with m.Case(0x9):
							m.d.comb += Assert(o_data == ord('9'))
						with m.Case(0xa):
							m.d.comb += Assert(o_data == ord('a'))
						with m.Case(0xb):
							m.d.comb += Assert(o_data == ord('b'))
						with m.Case(0xc):
							m.d.comb += Assert(o_data == ord('c'))
						with m.Case(0xd):
							m.d.comb += Assert(o_data == ord('d'))
						with m.Case(0xe):
							m.d.comb += Assert(o_data == ord('e'))
						with m.Case(0xf):
							m.d.comb += Assert(o_data == ord('f'))
				with m.Case(6):
					with m.Switch(data_copy[16:20]):
						with m.Case(0x0):
							m.d.comb += Assert(o_data == ord('0'))
						with m.Case(0x1):
							m.d.comb += Assert(o_data == ord('1'))
						with m.Case(0x2):
							m.d.comb += Assert(o_data == ord('2'))
						with m.Case(0x3):
							m.d.comb += Assert(o_data == ord('3'))
						with m.Case(0x4):
							m.d.comb += Assert(o_data == ord('4'))
						with m.Case(0x5):
							m.d.comb += Assert(o_data == ord('5'))
						with m.Case(0x6):
							m.d.comb += Assert(o_data == ord('6'))
						with m.Case(0x7):
							m.d.comb += Assert(o_data == ord('7'))
						with m.Case(0x8):
							m.d.comb += Assert(o_data == ord('8'))
						with m.Case(0x9):
							m.d.comb += Assert(o_data == ord('9'))
						with m.Case(0xa):
							m.d.comb += Assert(o_data == ord('a'))
						with m.Case(0xb):
							m.d.comb += Assert(o_data == ord('b'))
						with m.Case(0xc):
							m.d.comb += Assert(o_data == ord('c'))
						with m.Case(0xd):
							m.d.comb += Assert(o_data == ord('d'))
						with m.Case(0xe):
							m.d.comb += Assert(o_data == ord('e'))
						with m.Case(0xf):
							m.d.comb += Assert(o_data == ord('f'))
				with m.Case(7):
					with m.Switch(data_copy[12:16]):
						with m.Case(0x0):
							m.d.comb += Assert(o_data == ord('0'))
						with m.Case(0x1):
							m.d.comb += Assert(o_data == ord('1'))
						with m.Case(0x2):
							m.d.comb += Assert(o_data == ord('2'))
						with m.Case(0x3):
							m.d.comb += Assert(o_data == ord('3'))
						with m.Case(0x4):
							m.d.comb += Assert(o_data == ord('4'))
						with m.Case(0x5):
							m.d.comb += Assert(o_data == ord('5'))
						with m.Case(0x6):
							m.d.comb += Assert(o_data == ord('6'))
						with m.Case(0x7):
							m.d.comb += Assert(o_data == ord('7'))
						with m.Case(0x8):
							m.d.comb += Assert(o_data == ord('8'))
						with m.Case(0x9):
							m.d.comb += Assert(o_data == ord('9'))
						with m.Case(0xa):
							m.d.comb += Assert(o_data == ord('a'))
						with m.Case(0xb):
							m.d.comb += Assert(o_data == ord('b'))
						with m.Case(0xc):
							m.d.comb += Assert(o_data == ord('c'))
						with m.Case(0xd):
							m.d.comb += Assert(o_data == ord('d'))
						with m.Case(0xe):
							m.d.comb += Assert(o_data == ord('e'))
						with m.Case(0xf):
							m.d.comb += Assert(o_data == ord('f'))
				with m.Case(8):
					with m.Switch(data_copy[8:12]):
						with m.Case(0x0):
							m.d.comb += Assert(o_data == ord('0'))
						with m.Case(0x1):
							m.d.comb += Assert(o_data == ord('1'))
						with m.Case(0x2):
							m.d.comb += Assert(o_data == ord('2'))
						with m.Case(0x3):
							m.d.comb += Assert(o_data == ord('3'))
						with m.Case(0x4):
							m.d.comb += Assert(o_data == ord('4'))
						with m.Case(0x5):
							m.d.comb += Assert(o_data == ord('5'))
						with m.Case(0x6):
							m.d.comb += Assert(o_data == ord('6'))
						with m.Case(0x7):
							m.d.comb += Assert(o_data == ord('7'))
						with m.Case(0x8):
							m.d.comb += Assert(o_data == ord('8'))
						with m.Case(0x9):
							m.d.comb += Assert(o_data == ord('9'))
						with m.Case(0xa):
							m.d.comb += Assert(o_data == ord('a'))
						with m.Case(0xb):
							m.d.comb += Assert(o_data == ord('b'))
						with m.Case(0xc):
							m.d.comb += Assert(o_data == ord('c'))
						with m.Case(0xd):
							m.d.comb += Assert(o_data == ord('d'))
						with m.Case(0xe):
							m.d.comb += Assert(o_data == ord('e'))
						with m.Case(0xf):
							m.d.comb += Assert(o_data == ord('f'))
				with m.Case(9):
					with m.Switch(data_copy[4:8]):
						with m.Case(0x0):
							m.d.comb += Assert(o_data == ord('0'))
						with m.Case(0x1):
							m.d.comb += Assert(o_data == ord('1'))
						with m.Case(0x2):
							m.d.comb += Assert(o_data == ord('2'))
						with m.Case(0x3):
							m.d.comb += Assert(o_data == ord('3'))
						with m.Case(0x4):
							m.d.comb += Assert(o_data == ord('4'))
						with m.Case(0x5):
							m.d.comb += Assert(o_data == ord('5'))
						with m.Case(0x6):
							m.d.comb += Assert(o_data == ord('6'))
						with m.Case(0x7):
							m.d.comb += Assert(o_data == ord('7'))
						with m.Case(0x8):
							m.d.comb += Assert(o_data == ord('8'))
						with m.Case(0x9):
							m.d.comb += Assert(o_data == ord('9'))
						with m.Case(0xa):
							m.d.comb += Assert(o_data == ord('a'))
						with m.Case(0xb):
							m.d.comb += Assert(o_data == ord('b'))
						with m.Case(0xc):
							m.d.comb += Assert(o_data == ord('c'))
						with m.Case(0xd):
							m.d.comb += Assert(o_data == ord('d'))
						with m.Case(0xe):
							m.d.comb += Assert(o_data == ord('e'))
						with m.Case(0xf):
							m.d.comb += Assert(o_data == ord('f'))
				with m.Case(10):
					with m.Switch(data_copy[:4]):
						with m.Case(0x0):
							m.d.comb += Assert(o_data == ord('0'))
						with m.Case(0x1):
							m.d.comb += Assert(o_data == ord('1'))
						with m.Case(0x2):
							m.d.comb += Assert(o_data == ord('2'))
						with m.Case(0x3):
							m.d.comb += Assert(o_data == ord('3'))
						with m.Case(0x4):
							m.d.comb += Assert(o_data == ord('4'))
						with m.Case(0x5):
							m.d.comb += Assert(o_data == ord('5'))
						with m.Case(0x6):
							m.d.comb += Assert(o_data == ord('6'))
						with m.Case(0x7):
							m.d.comb += Assert(o_data == ord('7'))
						with m.Case(0x8):
							m.d.comb += Assert(o_data == ord('8'))
						with m.Case(0x9):
							m.d.comb += Assert(o_data == ord('9'))
						with m.Case(0xa):
							m.d.comb += Assert(o_data == ord('a'))
						with m.Case(0xb):
							m.d.comb += Assert(o_data == ord('b'))
						with m.Case(0xc):
							m.d.comb += Assert(o_data == ord('c'))
						with m.Case(0xd):
							m.d.comb += Assert(o_data == ord('d'))
						with m.Case(0xe):
							m.d.comb += Assert(o_data == ord('e'))
						with m.Case(0xf):
							m.d.comb += Assert(o_data == ord('f'))
				with m.Case(11):
					m.d.comb += Assert(o_data == ord('\n'))
				with m.Default():
					m.d.comb += Assert(0) # This should never happen

			"""
			Properties of data_copy
			"""
			# When idle, if i_stb is asserted, data_copy should take the value of
			# i_data on the next clock cycle
			with m.If(f_past_valid & (Past(state) == 0) & Past(self.i_stb)):
				m.d.comb += Assert(data_copy == Past(self.i_data))

			# During transmission, data_copy should remain stable regardless of changes
			# in i_data
			with m.If(f_past_valid & (Past(state) != 0) & (state != 0)):
				m.d.comb += Assert(Stable(data_copy))

			"""
			Properties of state
			"""
			# Initial state is idle
			with m.If(~f_past_valid):
				m.d.comb += Assert(state == 0)
			# The circuit never enters an invalid state
			m.d.comb += Assert(state < 12)
			# When idle, if i_stb was asserted in the previous clock cycle then the state
			# transitions to ZERO in this clock cycle
			with m.If(f_past_valid & (Past(state) == 0) & Past(self.i_stb)):
				m.d.comb += Assert(state == 1)
			# In every other state, a state transition is triggered if and only if counter
			# is nonzero and i_busy is de-asserted, and the state transitions are correct
			with m.If(f_past_valid & (Past(state) != 0) & \
				((Past(counter) == 0) | Past(i_busy))):
				m.d.comb += Assert(Stable(state))
			with m.If(f_past_valid & (Past(state) != 0) & \
				(Past(counter) != 0) & ~Past(i_busy)):
				m.d.comb += Assert(state == ((Past(state) + 1) % 12))

			"""
			Counter properties
			"""
			# Counter is always zero when idle
			with m.If(state == 0):
				m.d.comb += Assert(counter == 0)
			# Counter is always reset to zero between states
			with m.If(f_past_valid & ~Stable(state)):
				m.d.comb += Assert(counter == 0)
			# Otherwise, counter is always incrementing (under the current assumption with
			# a maximum number of consecutive busy cycles, such that the counter never
			# overflows)
			with m.If(f_past_valid & (state != 0) & Stable(state)):
				m.d.comb += Assert(counter == Past(counter) + 1)

		return m

class TXDataDemo(Elaboratable):
	"""
	Demo of TXData with event counter and change detector
	"""
	def elaborate(self, platform):
		m = Module()

		i_reset = Signal(1, reset=0)
		i_event = Signal(1, reset=0)
		io_counter = Signal(32, reset=0)
		m.submodules.counter = counter = Counter(i_reset, i_event, io_counter)

		io_stb = Signal(1, reset=0)
		io_data = Signal(32, reset=0)
		io_busy = Signal(1, reset=0)
		m.submodules.chgdetector = chgdetector = ChgDetector(io_counter, io_stb, \
			io_data, io_busy)

		o_uart_tx = Signal(1, reset=1)
		if platform is not None:
			o_uart_tx = platform.request('uart').tx.o
		m.submodules.txdata = txdata = TXData(io_stb, io_data, io_busy, o_uart_tx)

		ctr = Signal(28, reset=0)
		m.d.sync += i_event.eq(0)
		m.d.sync += ctr.eq(ctr + 1)
		with m.If(ctr == 0xFFFFFFF):
			m.d.sync += i_event.eq(1)

		return m

if __name__ == "__main__":
	"""
	Simulation
	"""
	m = Module()

	i_stb = Signal(1, reset=0)
	i_data = Signal(32, reset=0)
	o_busy = Signal(1, reset=0)
	o_uart_tx = Signal(1, reset=1)
	m.submodules.txdata = txdata = TXData(i_stb, i_data, o_busy, o_uart_tx)

	sim = Simulator(m)

	def process():
		for i in range(10):
			yield i_stb.eq(1)
			yield i_data.eq(9 * i)
			yield
			yield i_stb.eq(0)
			yield i_data.eq(0)
			yield
			while (yield o_busy):
				yield

	sim.add_clock(1e-8)
	sim.add_sync_process(process)

	with sim.write_vcd('txdata.vcd', 'txdata.gtkw', traces=txdata.ports()):
		sim.run()

	"""
	Formal Verification
	"""
	class TXDataTest(FHDLTestCase):
		def test_txdata(self):
			i_stb = Signal(1, reset=0)
			i_data = Signal(32, reset=0)
			o_busy = Signal(1, reset=0)
			o_uart_tx = Signal(1, reset=1)
			txdata = TXData(i_stb, i_data, o_busy, o_uart_tx, fv_mode=True)
			self.assertFormal(txdata, mode='prove', depth=18)
	TXDataTest().test_txdata()

	"""
	Build
	"""
	VersaECP5Platform().build(TXDataDemo(), do_program=True)