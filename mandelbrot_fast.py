#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import time

class Mandelbrot_fast():
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
		self.clr_values = None
		#self.array_x = np.zeros(self.res[0]*self.res[1])
		#self.array_y = np.zeros(self.res[0]*self.res[1])

	
	def construct_mandel(self):
		#numpy utilization!

		cx_array = np.linspace(self.xmin, self.xmax, self.res[0])
		cy_array = np.linspace(self.ymin, self.ymax, self.res[1])
		self.mandels_grid = np.meshgrid(cx_array, cy_array)
		c_array = self.mandels_grid[0] + self.mandels_grid[1] * 1j

		N=np.zeros_like(c_array)
		Z=np.zeros_like(c_array)
		for n in range(self.escape_time):
			i=np.less(Z.real**2+Z.imag**2, 2.0)
			N[i]=n
			Z[i]=Z[i]**2+c_array[i]
		self.clr_values=N.flatten()





	def save_fig(self, filename):
		"""
		Saves a mandelbrot scatter-plot as an image-file.
		"""
		
		# Normalizes the values of the color array
		self.clr_values = self.clr_values/(np.amax(self.clr_values)/1000)
		# Converts the array into an array of hex color values
		# The power on x is just to increase the color range
		clr_arr_hex = ["#%06x" % (int(x**2.2)) for x in self.clr_values.real]
		
		# Plots all the points calculated with corresponding color values
		plt.scatter(self.mandels_grid[0], self.mandels_grid[1], color=clr_arr_hex)
		plt.savefig(filename)
		print("\nImage saved as: {}".format(filename))

