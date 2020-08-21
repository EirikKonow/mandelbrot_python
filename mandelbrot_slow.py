#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
#import sys
from progressbar import progressbar



class Mandelbrot_slow():
	def __init__(self, xmin: float, xmax: float,
				ymin: float, ymax: float,
				res: (int, int), escape_time: int = 1000):

		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax
		self.res = res
		self.escape_time = escape_time
		self.mandels_grid = np.zeros(res)
		self.array_x = np.zeros(self.res[0]*self.res[1])
		self.array_y = np.zeros(self.res[0]*self.res[1])


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

		res_x = self.res[0]
		res_y = self.res[1]

		cx_range = np.linspace(self.xmin, self.xmax, res_x)
		cy_range = np.linspace(self.ymin, self.ymax, res_y)
		
		prog = 0
		prog_done = cx_range.size*cy_range.size

		for xIndex, xValue in enumerate(cx_range):
			for yIndex, yValue in enumerate(cy_range):
				self.mandels_grid[xIndex][yIndex] = self.mandelbrot_value(complex(xValue, yValue))
				self.array_x[prog] = xValue
				self.array_y[prog] = yValue
				prog+=1
				progressbar(prog, prog_done, 60)


	def save_fig(self, filename):
		"""
		Saves a mandelbrot scatter-plot as an image-file.
		"""
		
		clr_values = self.mandels_grid.flatten()
		
		# Normalizes the values of the color array
		clr_values = clr_values/(np.amax(clr_values)/1000)
		# Converts the array into an array of hex color values
		# The power on x is just to increase the color range
		clr_arr_hex = ["#%06x" % (int(x**2.2)) for x in clr_values]
		
		# Plots all the points calculated with corresponding color values
		plt.scatter(self.array_x, self.array_y, color=clr_arr_hex)
		plt.savefig(filename)
		print("\nImage saved as: {}".format(filename))



