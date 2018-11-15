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
        s.sendto(("3994\001IPS" + list).encode('utf-8'), addr)

    def connexion(self,run):

        
        data = ""
	list = ""
        while 1:
            if data == "quit":
                run=False
                s.close()
                break
            socks=[s]


            lin, lout, lex=select(socks, [stdin], [])

	    
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
	self.listban = []
        self.connection = {}

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
		    conn, addr = s.accept()


 		    contenu = data.split('/001')


		    cod = contenu[0]
	            commande = contenu[1]
		    contenu_commande = commande.split('#')

                    if data:
                        print(data)
		    	if C==3994 :
			    #on print la liste des ips
			    print("voici la liste des personnes connecté : ")

			    self.connection = commande
			    for element in M:
			        print(element[0])

			if C==4994 :
			    #on envoie un pm
			    if(nickname in listban):
     			    	print("contenu caché par bannissement")
                            else:
			        message = contenu_commande[1]
			    	print(message)
                            
			if C==5994 :
			    if(nickname in listban):
     			    	print("contenu caché par bannissement")
                            else:
			    #on envoie un bm
                            	message = contenu_commande[1]
			    	print(message)
			if C==994 :
			    #on ban
			   
                            

		
                   
            for x in lout:
		
		if select([stdin,],[],[],0.0)[0]:
		    if x == stdin :
		        data = stdin.readline().strip("\n")
		        #print ("entree clavier : %s" % data) 


			
			#lettre = input("Write your message")
			contenu = data.split(' ')


			cod = contenu[0]
			if(cod=="pm"):
			    codnumber = 4994
			if(cod=="bm"):
			    codnumber = 5994
			if(cod=="ban" or cod=="unban"):
			    codnumber = 6994
			
			

			


			if cod==4994 :
			    #on envoie un pm
			    nickname = contenu[1]
			    
     			    message = contenu[2]
			   
			    for name in connection:
			        if(name==nickname):
				    mess= "4994\001pm#"+nickname+message
				    s.sendto(message.encode('utf-8'), self.connection.get(name))
                            
			if cod==5994 :
			    #on envoie un bm
                            message = contenu[1]
			    for name in connection:
			        s.sendto(message.encode('utf-8'), self.connection.get(name))


			if cod == 6994:
    			    nikname = contenu[1]
                            if contenu_commande[0] == "ban":
                                listban.append(nikname)
                            elif contenu_commande[0] == "unban":
                                listban.remove(nikname)
			



		

    def start(self):
        s.sendto(("1994\001START"+ nickname).encode('utf-8'), (self.address, 1664))




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