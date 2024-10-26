import socket
import struct 

message= b'Hello, World!'
multicast_group = ('224.51.105.104', 10000)
ttl = 2

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.settimeout(2)
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
try: 
	print("sending {!r}".format(message))
	s.sendto(message, multicast_group)
	

	while True:
		print("Waiting to receive")
		try: 
			data, server = s.recvfrom(1024)
		except socket.timeout:
			print("timed out, no more responses")
			break
		else:
			print('received {!r} from{}'.format(data,server))
finally:
	print("closing socket")
	s.close()
	

