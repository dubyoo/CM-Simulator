#!/usr/bin/env python

from senddte import *
from time import time

if __name__ == '__main__':
	file = open('config.dat')
	file.next()
	
	t = time() - 1
	line_no = 0
	for line in file:
		line_no += 1
		list = line.split()
		if 0 == len(list):
			continue
		elif len(list) < 6:
			print "[ERROR] incomplete data in line %d: %s" % (line_no, line)
			continue
		
		param = Param()
		param.UDP_IP   = list[0]
		param.UDP_PORT = list[1]
		param.SGID     = list[2]
		param.MAC      = list[3]
		param.GROUP_IP = list[4]
		param.LEAVE_OR_JOIN = list[5]
		
		while time() - t < 0.5:
			continue
		t = time()
		senddte(param)
	
	file.close()
	