#!/usr/bin/env python

from socket import *
from sys import *

nickname = input("Your nickname, please: ")

class Serveur:

	nickname = ""
	
	def __init__(self, nom):
		self.nom = nom
		
	def connexion(address):
		s = socket(AF_INET, SOCK_STREAM)
        #s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		s.bind((address, 1664))
		#s.listen(5)
		
	def hello(addr):
		s.sendto(("HELLO" + self.nickname).encode('utf-8'), addr)
		
	def listAddress(self):
		clients = []
		while data:
			data, addr = s.recvfrom(1024)
			if addr not in clients:
				clients.append(addr)
			 #   nickname = data.decode('utf-8')
				#nickname = nickname.split(" ")
				#nickname = nickname[1]
				hello(addr);
			

		
class Client:

	s = socket(AF_INET, SOCK_STREAM)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	
	def __init__(self, nom, address):
		self.nom = nom
		self.address = address	
		
	def connexion(address):
		s.connect((address, 1664))
		
	def start(self):
		s.sendto(("START "+nickname).encode('utf-8'), (self.address,1664))
		
	
		
if len(argv) == 1:
	host = socket.gethostbyname(socket.gethostname())
	serveur = Serveur(nickname)
	serveur.connexion(host)
    serveur.listAddress()
	
	print(serveur.nom)
elif len(argv) == 2:
	client = Client(nickname, argv[1])
	client.connexion(argv[1])
	client.start()
	
