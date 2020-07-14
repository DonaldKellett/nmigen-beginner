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

from txuart import *
from rxuart import *
from sfifo import *

__all__ = ['LineTest', 'VersaECP5Platform']

"""
Line capturer using a FIFO
See http://zipcpu.com/tutorial/lsn-10-fifo.pdf for more details
"""

class LineTest(Elaboratable):
	def elaborate(self, platform):
		m = Module()

		state = Signal(1, reset=0)
		counter = Signal(2, reset=0)

		m.submodules.rxuart = rxuart = RXUART()
		m.submodules.sfifo = sfifo = SFIFO()
		m.submodules.txuart = txuart = TXUART()
		uart = platform.request('uart')
		rxuart.i_uart_rx = uart.rx.i
		txuart.o_uart_tx = uart.tx.o

		m.d.comb += sfifo.i_data.eq(rxuart.o_data)
		m.d.comb += sfifo.i_wr.eq(rxuart.o_stb & (sfifo.o_fill < 80) & (state == 0))
		m.d.comb += txuart.i_data.eq(sfifo.o_data)

		with m.FSM():
			with m.State('IDLE'):
				m.next = 'IDLE'
				with m.If(rxuart.o_stb & ((rxuart.o_data == ord('\n')) | (sfifo.o_fill >= 79))):
					m.next = 'PRINTLN'
					m.d.sync += state.eq(1)
			with m.State('PRINTLN'):
				m.next = 'PRINTLN'
				with m.If((counter == 0) & ~sfifo.o_empty):
					m.d.sync += sfifo.i_rd.eq(1)
					m.d.sync += counter.eq(1)
				with m.If(counter == 1):
					m.d.sync += sfifo.i_rd.eq(0)
					m.d.sync += txuart.i_wr.eq(1)
					m.d.sync += counter.eq(2)
				with m.If(counter == 2):
					m.d.sync += txuart.i_wr.eq(0)
					m.d.sync += counter.eq(3)
				with m.If((counter == 3) & ~txuart.o_busy):
					m.d.sync += counter.eq(0)
				with m.If((counter == 0) & sfifo.o_empty):
					m.next = 'IDLE'
					m.d.sync += state.eq(0)

		return m

if __name__ == '__main__':
	"""
	Build
	"""
	VersaECP5Platform().build(LineTest(), do_program=True)