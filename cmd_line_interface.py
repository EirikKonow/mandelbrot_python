#!/usr/bin/env python3

import argparse
import sys
from mandelbrot import Mandelbrot

def is_cmd_number(string):
	if type(string) == str:
		if string[0] == '-':
			string = string[1:len(string)]
	return string.replace('.','',1).isdigit()


def cmd_line_interface():
	"""
	A comprehensive commnad line interface for selecting a mandelbrot.


	Will either guide you through selecting all the values,
	or take command line arguments as input with the argparse module.
	"""

	if len(sys.argv) == 1:
		args = {}
		print(type(args))
		# Introduction
		msg ="""	{}
	# {:>58}
	# Welcome to my mandelbrot visualizer.{:>22}
	# To generate an image please insert{:>24}
	# the parameters needed to compute the values.{:>14}
	# {:>58}
	# Note: You can add all values at once as{:>19}
	# command-line arguments to skip this guide.{:>16}
	# {:>58}
	{}""".format('#'*60,'#','#','#','#','#','#','#','#','#'*60)

		print(msg)

		# Selecting version
		msg = """
	Select a version to use, current options are 1, 2, and 3.
	"""
		version = input(msg)

		while(not version in ['1','2','3']):
			print("	Invalid input!")
			version = input(msg)

		args["version"] = version
		print(type(args))
		print(args)


		# Selecting xmin
		msg = """
	Select the starting value of the x-axis
	in the graph, normally set between -2 and 1.
	"""
		xmin = input(msg)

		while(not is_cmd_number(xmin)):
			print("	Invalid input, needs to be a number!")
			xmin = input(msg)


		# Selecting xmax
		msg = """
	Select the max value of the x-axis
	in the graph, normally set between -2 and 1.
	"""
		xmax = input(msg)
		print()

		while(not is_cmd_number(xmax) or xmax<xmin):
			if not xmax.replace('.','',1).isdigit():
				print("	Invalid input, needs to be a number!",end='')
			else:
				print("	Max value needs to be bigger than starting value, current starting value is {}".format(xmin),end='')
			xmax = input(msg)
			print()
		
		xmin = float(xmin)
		xmax = float(xmax)
		args["xmin"] = xmin
		args["xmax"] = xmax


		# Selecting ymin
		msg = """
	Select the starting value of the y-axis
	in the graph, normally set between -1 and 1.
	"""
		ymin = input(msg)

		while(not is_cmd_number(ymin)):
			print("	Invalid input, needs to be a number!")
			ymin = input(msg)


		# Selecting ymax
		msg = """
	Select the max value of the y-axis
	in the graph, normally set between -1 and 1.
	"""
		ymax = input(msg)
		print()

		while(not is_cmd_number(ymax) or ymax<ymin):
			if not ymax.replace('.','',1).isdigit():
				print("	Invalid input, needs to be a number!",end='')
			else:
				print("	Max value needs to be bigger than starting value, current starting value is {}".format(ymin),end='')
			ymax = input(msg)
			print()
		
		ymin = float(ymin)
		ymax = float(ymax)
		args["ymin"] = ymin
		args["ymax"] = ymax

		# Selecting Nx
		msg = """
	Select the number of points to calculate
	along the x-axis, normally between 300 and 1000.
	"""
		nx = input(msg)
		print()

		while(not is_cmd_number(nx)):
			print("	Invalid input, needs to be a number!",end='')
			nx = input(msg)
			print()
		
		nx = int(nx)
		args["Nx"] = nx


		# Selecting Ny
		msg = """
	Select the number of points to calculate
	along the y-axis, normally between 300 and 1000.
	"""
		ny = input(msg)
		print()

		while(not is_cmd_number(ny)):
			print("	Invalid input, needs to be a number!",end='')
			ny = input(msg)
			print()
		
		ny = int(ny)
		args["Ny"] = ny

		# Selecting name
		msg = """
	Finally, select the name of the output file.
	"""
		name = input(msg)
		args["name"] = name


		# Runs the mandelbrot
		mandel = Mandelbrot(xmin, xmax, ymin, ymax, (nx, ny))
		mandel.construct_mandel()
		mandel.save_fig("mymandle")



	else:
		# argparse version of interface
		parser = argparse.ArgumentParser()
		parser.add_argument("version",
							help="select mandelbort version",
						   type = str)

		parser.add_argument("xmin",
							help="startpoint of x",
							type = float)

		parser.add_argument("xmax",
							help="endpoint of x",
							type = float)

		parser.add_argument("ymin",
							help="startpoint of y",
							type = float)

		parser.add_argument("ymax",
							help="endpoint of y",
							type = float)

		parser.add_argument("Nx",
							help="points computed in x-direction",
							type = int)
		
		parser.add_argument("Ny",
							help="points computed in y-direction",
							type = int)

		parser.add_argument("name",
							help="set name of image",
							type = str)

		args = parser.parse_args()

		# Constructs the filename
		version = "mandelbrot_" + args.version + ".py"

		print("Working method:")
		print(vars(args))
		print("version={}".format(version))

	
		# Runs the file
		exec(open(version).read(), vars(args))



"""
Working method:
{'version': '1', 'xmin': -1.0, 'xmax': 2.0, 'ymin': -1.0, 'ymax': 1.0, 'Nx': 100, 'Ny': 100, 'name': 'test1'}
version=mandelbrot_1.py

non-working method:
{'version': '1', 'xmin': -1.0, 'xmax': 2.0, 'ymin': -1.0, 'ymax': 1.0, 'Nx': 100, 'Ny': 100, 'name': 'test1'}
version=mandelbrot_1.py
"""