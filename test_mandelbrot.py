import numpy as np
import sys

def test_mandelbrot_outside(xmin, xmax, ymin, ymax, Nx, Ny):
	"""
	Checks if all values for c instantly are out of the mandelbrot set.
	"""
	
	cx_array = np.linspace(xmin, xmax, Nx)
	cy_array = np.linspace(ymin, ymax, Ny)
	c_array  = cx_array + cy_array*1j
	c_bools = abs(c_array) > 2
	if(all(c_bools == True)):
		print("The rectangle you are trying to compute isn't in the mandelbrot set.")
		exit(1)
	
	
test_mandelbrot_outside(3, 6, 3, 6, 200, 200)
test_mandelbrot_outside(-1, 1, -1, 1, 200, 200)