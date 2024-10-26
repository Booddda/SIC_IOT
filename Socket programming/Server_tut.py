import socket
import sys

def create_socket(host, port):
    try: 
        global s
        s = socket.socket()
    except socket.error as msg:
        print(str(msg))

def bind_socket(host, port):
    try:
        global s
        print("Binding the socket...")
        
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print(f"binding error: {str(msg)}, Retrying....")
        bind_socket(host, port)

def socket_accept():
    conn, address = s.accept()
    print(f"Conncetion has been established {address[0]}, {address[1]} ")
    conn.close()