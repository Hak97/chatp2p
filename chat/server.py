#!/usr/bin/env python

import socket, time

host = socket.gethostbyname(socket.gethostname())
port = 9090
print(host)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
clients = []

quit = False
print("[ Server started ]")

while not quit:
	data, addr = s.recvfrom(1024)

	if addr not in clients:
		clients.append(addr)

	#time = time.strftime("%Y-%m-%d;%H:%M:%S", time.localtime())

	print("["+addr[0]+"]=["+str(addr[1])+"]/",end="")
	print(data.decode('utf-8'))

	for client in clients:
		if addr != client:
			s.sendto(data, client)

	#print("\n[ Server stopped ]")
	#quit = True
s.close()