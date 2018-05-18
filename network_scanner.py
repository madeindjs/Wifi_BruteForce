#!/usr/bin/env python
# -*- coding: utf-8 -*-

# inspired by http://null-byte.wonderhowto.com/how-to/build-arp-scanner-using-scapy-and-python-0162731/

import sys
from datetime import datetime

from scapy.all import srp,Ether,ARP,conf

def scan_ips(interface='wlan0', ips='192.168.1.0/24'):
	"""a simple ARP scan with Scapy"""
	try:
		print('[*] Start to scan')
		conf.verb = 0 # hide all verbose of scapy
		ether = Ether(dst="ff:ff:ff:ff:ff:ff")
		arp = ARP(pdst = ips)
		answer, unanswered = srp(ether/arp, timeout = 2, iface = interface, inter = 0.1)

		for sent, received in answer:
			print(received.summary())

	except KeyboardInterrupt:
		print('[*] User requested Shutdown')
		print('[*] Quitting...')
		sys.exit(1)
