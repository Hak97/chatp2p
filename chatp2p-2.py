#!/usr/bin/env python

from socket import *
from sys import *

nickname = input("Your nickname, please: ")
s = socket(AF_INET, SOCK_STREAM)


class Serveur:

    def __init__(self, nom):
        self.nom = nom
        self.connection = []

    def genisis(self, address):
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((address, 1664))
        s.listen(5)
        #conn, addr = s.accept()

    def connexion(self):
        conn, addr = s.accept()
        if conn not in self.connection:
            self.connection.append(conn)
        for i in self.connection:
            print(i)

    def hello(addr):
        s.sendto(("HELLO" + nickname).encode('utf-8'), addr)

    def listAddress(self):
        clients = []
        while True:
            print(s.recvfrom(1024))
            data, addr = s.recvfrom(1024)
            if addr not in clients:
                clients.append(addr)
                #   nickname = data.decode('utf-8')
                # nickname = nickname.split(" ")
                # nickname = nickname[1]
                self.hello(addr);




class Client:
    # s = socket(AF_INET, SOCK_STREAM)
    # s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def __init__(self, nom, address):
        self.nom = nom
        self.address = address

    def connexion(self, address):
        s.connect((address, 1664))

    def start(self):
        s.sendto(("START " + nickname).encode('utf-8'), (self.address, 1664))


if len(argv) == 1:
    host = gethostbyname(gethostname())
    print (host)
    serveur = Serveur(nickname)
    serveur.genisis(host)
    print(serveur.nom)
    while True:
        serveur.connexion()


elif len(argv) == 2:
    client = Client(nickname, argv[1])
    print(argv[1])
    client.connexion(argv[1])
    client.start()
