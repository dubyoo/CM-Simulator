#!/usr/bin/env python

from socket import *
import sys

class Param:
	def __init__(self):
		self.UDP_IP = ""
		self.UDP_PORT = ""
		self.SGID = ""
		self.MAC = ""
		self.GROUP_IP = ""
		self.LEAVE_OR_JOIN = ""


def print_str(message, param):
	print "[DEBUG] send to %s(%s):" % (param.UDP_IP, param.UDP_PORT)
	for c in message:
		if '\r' == c:
			sys.stdout.write("\\r")
		elif '\n' == c:
			sys.stdout.write("\\n")
		else:
			sys.stdout.write(c)
	sys.stdout.write("\n\n")
	sys.stdout.flush()


def senddte(param):
	if param.LEAVE_OR_JOIN == "join":
		param.LEAVE_OR_JOIN = "0"
	elif param.LEAVE_OR_JOIN == "leave":
		param.LEAVE_OR_JOIN = "1"
	else:
		print "[ERROR] unknown param in [leave_or_join]:", param.LEAVE_OR_JOIN
		sys.exit()

	payload = "message_payload: session_id=" + param.LEAVE_OR_JOIN + "; client_destination=192.26.14.1; client_cablemodem_mac_address=" + param.MAC + "; " + "source_ip=" + param.GROUP_IP + ";retry_count=2;rc_index=1;rc_chan_freq=480000000; client_cpe_destination=10.90.242.82;" + "cm_vednor=name;cm_type=1;sgid=" + param.SGID + "\r\n"
	content_length = len(payload)
	head = "SETUP rtsp://hlit.net RTSP/1.0\r\nCSeq: 313\r\nRequire: com.harmonic.d2e.ccp\r\nHeader: protocolDescriminator=17;dsmcc_type=4;message_id=1;transaction_id=393;\r\nContent-Length: " + str(content_length) + "\r\n\r\n"

	message = head + payload

	print_str(message, param)

	sock = socket(AF_INET, SOCK_DGRAM)
	sock.sendto(message, (param.UDP_IP, int(param.UDP_PORT)))


# senddte [IP] [Port] [SGID] [mac] [group_ip] [leave_or_join]
if __name__ == '__main__':
	if len(sys.argv) < 7:
		print "USAGE :", sys.argv[0], "[IP] [Port] [SGID] [MAC] [group_ip] [leave_or_join]"
		print "SAMPLE:", sys.argv[0], "10.90.242.246 22408 100 00-1C-26-C8-5C-50 238.1.1.1 join"
		sys.exit()

	param = Param()
	param.UDP_IP   = sys.argv[1]
	param.UDP_PORT = sys.argv[2]
	param.SGID     = sys.argv[3]
	param.MAC      = sys.argv[4]
	param.GROUP_IP = sys.argv[5]
	param.LEAVE_OR_JOIN = sys.argv[6]

	senddte(param)

	sys.exit()
