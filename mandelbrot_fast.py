#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
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
		self.map = np.zeros((self.res[0],self.res[1]))


	def meshgrid(self, *xi, copy=True, sparse=False, indexing='xy'):
		"""
		Borrowing the meshgrid function from numpy 
		since meshgrid isn't directly supported by numba.
		Source:
		https://github.com/numpy/numpy/blob/v1.19.0/numpy/lib/function_base.py#L4102-L4229
		"""
		ndim = len(xi)

		if indexing not in ['xy', 'ij']:
		    raise ValueError(
		        "Valid values for `indexing` are 'xy' and 'ij'.")

		s0 = (1,) * ndim
		output = [np.asanyarray(x).reshape(s0[:i] + (-1,) + s0[i + 1:])
		          for i, x in enumerate(xi)]

		if indexing == 'xy' and ndim > 1:
		    # switch first and second axis
		    output[0].shape = (1, -1) + s0[2:]
		    output[1].shape = (-1, 1) + s0[2:]

		if not sparse:
		    # Return the full N-D matrix (not only the 1-D vector)
		    output = np.broadcast_arrays(*output, subok=True)

		if copy:
		    output = [x.copy() for x in output]

		return output

	def construct_mandel(self):
		#numpy utilization!

		cx_array = np.linspace(self.xmin, self.xmax, self.res[0])
		cy_array = np.linspace(self.ymin, self.ymax, self.res[1])
		
		#self.mandels_grid = np.meshgrid(cx_array, cy_array)
		#c_array = self.mandels_grid[0] + self.mandels_grid[1] * 1j

		mandels_grid_0, mandels_grid_1 = self.meshgrid(cx_array, cy_array)
		c_array = mandels_grid_0 + mandels_grid_1 * 1j
		print(c_array)

		N=np.zeros_like(c_array)
		Z=np.zeros_like(c_array)
		for n in range(self.escape_time):
			i=np.less(Z.real**2+Z.imag**2, 2.0)
			N[i]=n
			Z[i]=Z[i]**2+c_array[i]
		self.clr_values=N.flatten()





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

		"""
	def mandelbrot_calculation(self, z: complex, c: complex) -> complex:
		"""
		#Computes a iteration for a point in the mandlebrot set
		
		#mandelbrot(z, c) = z**2 + c
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
		#numpy utilization!

		#cx_array = np.linspace(self.xmin, self.xmax, self.res[0])
		#cy_array = np.linspace(self.ymin, self.ymax, self.res[1])
		#self.mandels_grid = np.meshgrid(cx_array, cy_array)
		c_array = self.mandels_grid[0] + self.mandels_grid[1] * 1j

		cx_range = np.linspace(self.xmin, self.xmax, self.res[0])
		cy_range = np.linspace(self.ymin, self.ymax, self.res[1])
		#self.map = []

		prog = 0
		prog_total = self.res[0]*self.res[1]
		for xIndex, xValue in enumerate(cx_range):
			for yIndex, yValue in enumerate(cy_range):
				self.map[yIndex][xIndex] = self.mandelbrot_value(complex(xValue, yValue))




	def save_fig(self, filename):
		
		# Plots all the points calculated with corresponding color values
		#plt.scatter(self.mandels_grid[0], self.mandels_grid[1], marker="+", color=cmap(norm(self.clr_values.real)))
		#plt.savefig(filename, dpi=2000)
		#self.map = np.array(self.map)
		plt.imshow(self.map, cmap = "viridis")
		plt.show()
		print("\nImage saved as: {}".format(filename))

		"""