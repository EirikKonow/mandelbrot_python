#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import time
from numba.experimental import jitclass
from numba import int32, float32, float64
import numba as nb


spec = [
	('xmin', float32),
	('xmax', float32),
	('ymin', float32),
	('ymax', float32),
	('resx', int32),
	('resy', int32),
	('escape_time', int32),
	('mandels_grid', float64[:,:]),
	('clr_values', float64[:]),
	('array_x', float64[:]),
	('array_y', float64[:]),
]

@jitclass(spec)
class Mandelbrot_faster():
	def __init__(self, xmin: float, xmax: float,
				ymin: float, ymax: float,
				res: (int, int), escape_time: int = 1000):

		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax
		self.resx = res[0]
		self.resy = res[1]
		self.escape_time = escape_time
		self.mandels_grid = np.zeros((self.resx, self.resy))
		self.clr_values = np.zeros(self.resx*self.resy)
		self.array_x = np.zeros(self.resx*self.resy)
		self.array_y = np.zeros(self.resx*self.resy)
		#self.clr_arr_hex = np.chararray(self.resx*self.resy)
		#self.clr_arr_hex = empty_int64_list()


	def mandelbrot_calculation(self, z: complex, c: complex) -> complex:
		"""
		Computes a iteration for a point in the mandlebrot set
		
		mandelbrot(z, c) = z**2 + c
		"""
		
		re = z.real**2 - z.imag**2 + c.real
		im = 2 * z.real * z.imag + c.imag
		return complex(re, im)


	def mandelbrot_value(self, c: complex) -> int:
		val = self.escape_time
		f = complex(0,0)
		while val > 0:
			f = self.mandelbrot_calculation(f,c)
			if abs(f) > 2:
				return val
			val = val -1

		return val
		

	def construct_mandel(self):
		z = complex(0,0)

		cx_range = np.linspace(self.xmin, self.xmax, self.resx)
		cy_range = np.linspace(self.ymin, self.ymax, self.resy)
		

		for xIndex, xValue in enumerate(cx_range):
			for yIndex, yValue in enumerate(cy_range):
				self.mandels_grid[xIndex][yIndex] = self.mandelbrot_value(complex(xValue, yValue))
				self.array_x[xIndex+xIndex*yIndex] = xValue
				self.array_y[xIndex+xIndex*yIndex] = yValue


	def save_fig(self, filename):
		"""
		#Saves a mandelbrot scatter-plot as an image-file.
		"""

		
		cmap = plt.cm.hsv
		norm = matplotlib.colors.Normalize(vmin=0, vmax=30)
		
		# Converts the array into an array of hex color values
		#The power on x is just to increase the color range
		#clr_arr_hex = ["#%06x" % (int(x**2.2)) for x in self.clr_values]
		plt.scatter(self.mandels_grid[0], self.mandels_grid[1], marker="+", color=cmap(norm(self.clr_values.real)))
		plt.savefig(filename, dpi=1000)