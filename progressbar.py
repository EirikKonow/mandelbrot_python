def progressbar(current, total, barLength = 20):
	"""
	A progress bar.


	Taken from https://stackoverflow.com/questions/6169217/replace-console-output-in-python
	"""

	percent = float(current) * 100 / total
	arrow   = '-' * int(percent/100 * barLength - 1) + '>'
	spaces  = ' ' * (barLength - len(arrow))

	print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')