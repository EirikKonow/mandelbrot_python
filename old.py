#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import time
from numba import jit


@jit(nopython=True)
def mandelbrot(z: complex, c: complex) -> complex:
	"""
	Computes a iteration for a point in the mandlebrot set
	
	mandelbrot(z, c) = z**2 + c
	"""
	
	re = z.real**2 - z.imag**2 + c.real
	im = 2 * z.real * z.imag + c.imag
	return complex(re, im)

@jit(nopython=True)
def create_grid(xmin: float, xmax: float,
				ymin: float, ymax: float,
				res: (int, int),
				escape_time: int = 1000) -> (np.ndarray, np.ndarray, np.ndarray):
	"""
	Creates a grid of numbers corresponding to the mandelbrot set.
	
	
	Runs thorugh all values of z=x+yi in the complex plain and gives
	a value back based on if it's in or how fast it was computed out
	of the set.
	"""
	
	z = complex(0,0)
	
	# Number of points in the x and y range
	res_x = res[0]
	res_y = res[1]
	
	# All values of x and y
	cx_range = np.linspace(xmin, xmax, res_x)
	cy_range = np.linspace(ymin, ymax, res_y)

	# Empty x*y array for mandelbrot values
	mandels_grid = np.zeros((res_x, res_y))

	# Empty 1d arrays for all x and y values
	array_x = np.zeros(res_x*res_y)
	array_y = np.zeros(res_x*res_y)
	
	# Initial postition values for the 3 arrays
	pos = 0
	pos_x = 0
	pos_y = 0

	# Iterates through all c=x+yi values and checks if they
	# are in the mandelbrot set, adds their value to the grid.
	for i in cx_range:
		for j in cy_range:
			clr = escape_time
			c = complex(i, j)
			f = complex(0, 0)
			for j in range(escape_time):
				f = mandelbrot(f, c)
				if abs(f) > 2:
					mandels_grid[pos_x][pos_y] = clr
					break
				else:
					if j == escape_time-1:
						mandels_grid[pos_x][pos_y] = clr
						pass
				clr = clr - 1
			array_x[pos] = c.real
			array_y[pos] = c.imag
			pos_y += 1
			pos += 1
		pos_x += 1
		pos_y = 0
		
	return array_x, array_y, mandels_grid
	
def save_fig(x_vals, y_vals, clr_grid, filename, mode=1):
	"""
	Saves a mandelbrot scatter-plot as an image-file.
	"""
	
	clr_values = clr_grid.flatten()
	
	# Normalizes the values of the color array
	clr_values = clr_values/(np.amax(clr_values)/1000)
	# Added modes for assignment 4.7
	if(mode==1):
		# Converts the array into an array of hex color values
		# The power on x is just to increase the color range
		clr_arr_hex = ["#%06x" % (int(x**2.2)) for x in clr_values]
	if(mode==2):
		clr_arr_hex = ["#%06x" % (int(x**1.5)) for x in clr_values]
	if(mode==3):
		clr_arr_hex = ["#%08x" % (int(x**2.2)) for x in clr_values]
	
	# Plots all the points calculated with corresponding color values
	plt.scatter(x_vals, y_vals, color=clr_arr_hex)
	plt.savefig(filename)
	

# For when ran by itself, or via mandelbrot.py
if __name__=="__main__" or len(sys.argv) > 8:
	
	if(len(sys.argv)) == 9:
		xmin = float(sys.argv[2])
		xmax = float(sys.argv[3])
		ymin = float(sys.argv[4])
		ymax = float(sys.argv[5])
		res = int(sys.argv[6]), int(sys.argv[7])
		filename = sys.argv[8]
	else:
		xmin = -2
		xmax = 2
		ymin = -2
		ymax = 2
		res = (300, 300)
		filename = "image_mandel.png"

	start = time.time()
	values = create_grid(xmin, xmax, ymin, ymax, res)
	stop = time.time()
	print(stop-start)

	save_fig(values[0], values[1], values[2], filename)
