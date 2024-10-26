import socket
import struct 

multicast_group = '224.51.105.104'
server_address = ('',10000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

s.bind(server_address )
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
while True:
	print("Waiting to receive") 
	data, address= s.recvfrom(1024)
	print('received {} bytes from{}'.format(len(data),address))
	print(data)
	
	print("sending ack to", address)
	s.sendto(b'ack', address)
	

