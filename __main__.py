from wifi import Cell, Scheme, exceptions

if __name__ == '__main__':

	# need `sudo` to show all networks
	for cell in Cell.all('wlan0'):
		
		try:
			scheme = Scheme.for_cell('wlan0', 'home', cell, 'test')
			scheme.activate()
		except exceptions.ConnectionError as e:
			print("Can't connect to {} with `{}` passkey".format(cell, 'test'))
		