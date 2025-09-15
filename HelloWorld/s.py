#a socket is an endpoint for sending or receiving data across a network. Mainly used for communication between a client and a server. It allows data exchange over the internet or local networks. Important for network programming and building applications that require data transfer.

import socket

HOST = 'localhost'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is for IPv4, SOCK_STREAM is for TCP/port

s.connect((HOST, PORT))

