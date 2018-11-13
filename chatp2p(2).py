#!/usr/bin/env python
# coding: utf8

from socket import *
from sys import *
from select import *


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

    def hello(self, addr, s):
        s.sendto(("HELLO " + nickname).encode('utf-8'), addr)

    def ips(self, addr, s, list):
        s.sendto(("IPS " + list).encode('utf-8'), addr)

    def connexion(self):
        conn, addr = s.accept()
        print(addr)
        if conn not in self.connection:
            self.hello(addr, conn)
            self.connection.append(addr[0])
            data = conn.recv(1024)
            print(data)
        list = ""
        count = 0
        for i in self.connection:
            count = count + 1
            list = list + i
            if count != len(self.connection):
                list = list + ","
        print(list)
        self.ips(addr, conn, list)
        
        



class Client:
    # s = socket(AF_INET, SOCK_STREAM)
    # s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def __init__(self, nom, address):
        self.nom = nom
        self.address = address

    def connexion(self, address):
        s.connect((address, 1664))

    def receive(self):
            while True:
                    data = s.recv(1024)
                    if data:
                        print(data)

    def start(self):
        s.sendto(("START " + nickname).encode('utf-8'), (self.address, 1664))




if len(argv) == 1:
    data = ""
    while 1:
        if data == "exit":
            break
        lin, lout, lex =select([stdin],[],[])
        for x in lin:
            if x==stdin :
                data = stdin.readline().strip("\n")
                print ("entrée clavier : %s" % data)
    host = gethostbyname(gethostname())
    print (host)
    serveur = Serveur(nickname)
    serveur.genisis(host)
    print(serveur.nom)
    
    while True:
        #serveur.connexion()
        data = ""
        while 1:
            if data == "exit":
                break
            lin, lout, lex =select([stdin],[],[])
            for x in lin:
                if x == stdin :
                    data = stdin.readline().strip("\n")
                    print ("entrée clavier : %s" % data)

elif len(argv) == 2:
    client = Client(nickname, argv[1])
    print(argv[1])
    client.connexion(argv[1])
    client.start()
    client.receive()