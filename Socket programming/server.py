import socket

ADDRESS = ("127.0.0.1",5005)
MESSAGE = b"Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind(ADDRESS)

while True:
	data, addr = s.recvfrom(1024) 
	print("received message: {}" .format(data))