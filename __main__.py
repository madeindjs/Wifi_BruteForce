#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import wifi_bruteforce
import network_scanner

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-w", "--wifi_brute_force", action="store_true", help="Try to brute force all wifi detected by this device")
	parser.add_argument("-a", "--scan_ips", action="store_true", help="Scan all IPs on this networks")
	args = parser.parse_args()

	if args.wifi_brute_force:
		wifi_bruteforce.start()

	if args.scan_ips:
		network_scanner.scan()



if __name__ == '__main__':
	main()