#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from wifi import Cell, Scheme, exceptions

if __name__ == '__main__':

	nb_test = 0

	# need `sudo` to show all networks
	for cell in Cell.all('wlan0'):

		try:
			scheme = Scheme.for_cell('wlan0', 'home', cell, 'test')
			scheme.activate()
			print("Connect to {} with `{}` passkey works!!".format(cell, 'test'))
			sys.exit(0)
		except exceptions.ConnectionError as e:
			pass
		finally:
			nb_test += 1

		sys.stdout.write('\rtest n°{}'.format( nb_test ))
		sys.stdout.flush()

	print("you are not lucky :'(")
		