#!/usr/bin/env python
# coding: utf8

from socket import *
from sys import *
from sys import stdin
from select import *


nickname = raw_input("Your nickname, please: ")
s = socket(AF_INET, SOCK_STREAM)


class Serveur:

    def __init__(self, nom):
        self.nom = nom
        self.connection = {}

    def genisis(self, address):
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((address, 1664))
        s.listen(5)

    def hello(self, addr, s):
        s.sendto(("HELLO " + nickname).encode('utf-8'), addr)

    def ips(self, addr, s, list):
        s.sendto(("IPS " + list).encode('utf-8'), addr)

    def broadcast(self,message):
        for clients in self.connection:
    
             clients.send(bytes(name,"utf-8")+message)


    def closing(self):
        message="quit"
        for name in self.connection: 
            # s.sendto(message.encode('utf8'),self.connection.get(name))
             self.broadcast(message)


    def connexion(self,run):

        
        data = ""
        list = ""
        message="quit"
        while 1:
            if data == "quit":
                print("quit")
                self.closing()
               
                run=False
                s.close()
                break
            socks=[s]


            lin, lout, lex=select(socks, [stdin], [])
            client_liste=[5]
        
            for t in lin:
                if t==s: 
                    conn, addr = s.accept()
                    print(addr)
                    if conn not in self.connection:
                        self.hello(addr, conn)
                        #self.connection.append(addr[0])
                        data = conn.recv(1024)
                        lst = data.split()
                        self.connection[lst[1]] = addr[0]

                        print(self.connection)
                    
                        count = 0
                        for i in self.connection:
                            count = count + 1
                            list = list + i
                            if count != len(self.connection):
                                list = list + ","
                        
                        self.ips(addr, conn, list)
                
                           
            for x in lout:
                
                if select([stdin,],[],[],0.0)[0]:
                    if x == stdin :
                        data = stdin.readline().strip("\n")
                        print ("entree clavier : %s" % data)   
                
                             
                      
            
            



class Client:
    # s = socket(AF_INET, SOCK_STREAM)
    # s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def __init__(self, nom, address):
        self.nom = nom
        self.address = address
        self.listban = {}

    def connexion(self, address):
        s.connect((address, 1664))
  
 

    def receive(self):
                    
        data = ""
    
        while 1:
            if data == "quit":
                run=False
                s.close()
                break
            socks=[s]


            lin, lout, lex=select(socks, [stdin], [])

        
            for t in lin:
                if t==s: 
                    data = s.recv(1024)
                    if data:
                        print(data)
        
                   
            for x in lout:
          
                if select([stdin,],[],[],0.0)[0]:
                    if x == stdin :
                        data = stdin.readline().strip("\n")
                        print ("entree clavier : %s" % data) 


        

    def start(self):
        s.sendto(("START " + nickname).encode('utf-8'), (self.address, 1664))




if len(argv) == 1:
    # data = ""
    # while 1:
    #     if data == "exit":
    #         break
    #     lin, lout, lex =select([stdin],[],[])
    #     for x in lin:
    #         if x==stdin :
    #             data = stdin.readline().strip("\n")
    #             print ("entrée clavier : %s" % data)
    host = gethostbyname(gethostname())
    print (host)
    serveur = Serveur(nickname)
    serveur.genisis(host)
    print(serveur.nom)
    run=True
    while run:
        run=serveur.connexion(run)

       

elif len(argv) == 2:
    client = Client(nickname, argv[1])
    print(argv[1])
    client.connexion(argv[1])
    client.start()
    client.receive()