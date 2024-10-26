import socket

ADDRESS = ("127.0.0.1",5005)
MESSAGE = b"Hello, World!"

print("UDP target IP: {}" .format(ADDRESS[0]))
print("UDP target port: {}" .format(ADDRESS[1]))
print("message: {!r}" .format(MESSAGE))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(MESSAGE, ADDRESS)