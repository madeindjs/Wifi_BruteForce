#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import wifi_bruteforce

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-w", "--wifi_brute_force", action="store_true", help="Try to brute force all wifi detected by this device")
	args = parser.parse_args()

	if args.wifi_brute_force:
		wifi_bruteforce.start()



if __name__ == '__main__':
	main()