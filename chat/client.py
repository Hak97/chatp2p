#!/usr/bin/env python

import socket, time

shutdown = False
join = False

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("127.0.0.1", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)
alias = input("name: ")

while shutdown==False:
	if join==False:
		s.sendto(("["+alias+"] => join chat ").encode('utf-8'), server)
		join=True
	else:
		message = input()
		if message == "quit":
			s.sendato(("["+alias+"] <= left chat").encode('utf-8'), server)
			shutdown == True
			break
		if message != "":
			s.sendto(("["+alias+"] :: "+message).encode('utf-8'), server)
			
while not shutdown:
	while True:
		data, addr = s.recvfrom(1024)
		print(data.decode('utf-8'))

s.close()



