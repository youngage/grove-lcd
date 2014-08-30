#!/usr/bin/python
# -*- charset: utf-8 -*-
# This is a port of https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight
# (c) 2014 Helge Jung <helge.jung@youngage.eu>
# Released unter the LGPL, like the original.

from smbus import SMBus

class Backlight(object):
	REG_RED		= 0x04 # pwm2
	REG_GREEN	= 0x03 # pwm1
	REG_BLUE	= 0x02 # pwm0

	REG_MODE1	= 0x00
	REG_MODE2	= 0x01
	REG_OUTPUT	= 0x08

	def __init__(self, bus, address):
		if not isinstance(bus, SMBus):
			raise TypeError

		self.bus = bus
		self.address = int(address)

		# initialize
		self.setRegister(self.REG_MODE1, 0)
		self.setRegister(self.REG_MODE2, 0)

		# all LED control by PWM
		self.setRegister(self.REG_OUTPUT, 0xAA)

	def setRegister(self, addr, value):
		self.bus.write_byte_data(self.address, addr, value)

	def setColor(self, red, green, blue):
		r = int(red)
		g = int(green)
		b = int(blue)
		self.setRegister(self.REG_RED, r)
		self.setRegister(self.REG_GREEN, g)
		self.setRegister(self.REG_BLUE, b)


if __name__ == '__main__':
	import time

	bus = SMBus(1)
	light = Backlight(bus, 0x62)

	light.setColor(255, 0, 0)
	time.sleep(1)
	light.setColor(0,255,0)
	time.sleep(1)
	light.setColor(0,0,255)
	time.sleep(1)
	light.setColor(255,0,255)
	time.sleep(1)
	light.setColor(255,255,255)
	time.sleep(1)
	light.setColor(0, 0, 128)
