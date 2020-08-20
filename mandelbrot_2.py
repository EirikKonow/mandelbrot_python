#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import sys
import time


def calc_f(z, c):
	f = z**2+c
	return f

def mandelbrot(z: complex, c: complex, escape_time: int = 1000) -> complex:
	clr = escape_time
	f = calc_f(z, c)
	for i in range(escape_time):
		if abs(f) <= 2:
			clr -= 1
			f = calc_f(f, c)
		else:
			break
	return clr

def save_fig(x_vals, y_vals, clr_grid, filename):
	"""
	Saves a mandelbrot scatter-plot as an image-file.
	"""
	
	clr_values = clr_grid
	
	# Normalizes the values of the color array
	clr_values = clr_values/(np.amax(clr_values)/1000)
	# Converts the array into an array of hex color values
	# The power on x is just to increase the color range
	clr_arr_hex = ["#%06x" % (int(x**2.2)) for x in clr_values]
	
	# Plots all the points calculated with corresponding color values
	plt.scatter(x_vals, y_vals, color=clr_arr_hex)
	plt.savefig(filename)



# For when ran by itself, or via mandelbrot.py
if __name__=="__main__" or len(sys.argv) == 9:
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
	
	z = complex(0,0)
	cx_array = np.linspace(xmin, xmax, res[0])
	cy_array = np.linspace(ymin, ymax, res[1])
	c_array = cx_array + cy_array*1j

	c_grid = np.meshgrid(cx_array, cy_array)

	c_array = c_grid[0] + c_grid[1] * 1j

	clr_array = c_array.flatten()
	clr_array = [mandelbrot(z, c) for c in clr_array]

	stop = time.time()
	print(stop-start)
	
	save_fig(c_grid[0], c_grid[1], clr_array, filename)
