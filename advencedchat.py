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
        self.listban = []
        self.socks=[]
        self.addresse = ''


    def genisis(self, address):
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((address, 1664))
        s.listen(5)
        self.addresse = address	


    def hello(self, addr, s):
	
        s.sendto(("2994\001HELLO#" + nickname).encode('utf-8'), addr)

    def ips(self, s, list):
        s.send(("3994\001IPS#" + list).encode('utf-8'))



    def connexion(self,run):
    	self.socks=[s]
        self.connection[self.nom] = self.addresse
        # self.listConn.append("")
        data = ""
        list = ""
        while 1:
            if data == "quit":
                run=False
                s.close()
                break
            


            lin, lout, lex=select(self.socks, [stdin], [])

	    
            for t in lin:
                if t==s: 
                    conn, addr = s.accept()
                    print(conn)
                    if conn not in self.socks:
	                	self.hello(addr, conn)
			
						data = conn.recv(1024)
			
						contenu = data.split('\001')
						# print(contenu)
						commande = contenu[1]
						contenu_commande = commande.split('#')
						print(contenu_commande[0]+ " " +contenu_commande[1])
						self.connection[contenu_commande[1]] = addr[0]
						self.socks.append(conn) #on ajoute les connections des sockets
						print(self.connection)
		    

						listNickIPs = ""
						#on remplie la chaine de nicknames et IPs
						count = 0
						for name in self.connection:
							count = count + 1
			    			listNickIPs = listNickIPs + name + ":" + self.connection.get(name)
			    			if count != len(self.connection):
							 	listNickIPs = listNickIPs + ","
			    

						print("Chaine de nicknames et IPs ", listNickIPs)
						count = 0
						for i in self.connection:
							count = count + 1 
							list = list + i
			    			if count != len(self.connection):
			        			list = list + ","						
						for conn in socks :
							self.ips(conn, listNickIPs)
		    		
                   
            for x in lout:
		
				if select([stdin,],[],[],0.0)[0]:
		    
					if x == stdin :
						data = stdin.readline().strip("\n")
		        		#print ("entree clavier : %s" % data) 
			

			
						#lettre = input("Write your message")
						contenu = data.split(' ')


						cod = contenu[0]
						print(cod) 
						if cod=="pm" :
						    codnumber = 4994
						elif cod=="bm" :
						    codnumber = 5994
						elif cod=="ban" or cod=="unban" :
						    codnumber = 6994
						else:
						    codnumber = 0
						    print("Votre commande est invalide (bm ... / pm nic ... / ban nic / unban nic)")
						
						    


						if codnumber==4994 :
			    			#on envoie un pm
							count = 0
			    			nickname = contenu[1]
			    
     			    		message = contenu[2]
     			    		for name in self.connection:
			        			if name==nickname :
				    				mess= "4994\001pm#"+nickname+"#"+message
				    				# if  self.listConn[count]!="":
				        			self.listConn[count].send((mess).encode('utf-8'))
								count = count + 1
						# elif codnumber==5994 :                                       	
			   # 				on envoie un bm
			   # 				count = 0
			   #  			print(self.connection)
      #                       message = contenu[1]
			   #  			for name in self.connection:
						# 		#print
						# 		print((self.connection.get(name),1664))
						# 		mess = "5994\001bm#"+message
						# 		commandsend = 5994
						# 		if self.listConn[count]!="":
			   #          			self.listConn[count].send((mess).encode('utf-8')) 
						# 		count = count + 1
						# elif codnumber == 6994:
    		# 	    		nikname = contenu[1]
			   #  			print(nikname)
      #                       if cod == "ban":
      #                           self.listban.append(nikname)
      #                       elif cod == "unban":
      #                           self.listban.remove(nikname)
   
		
		             
              
    
	



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
    	# host = gethostbyname(gethostname())
     #    server=socket(AF_INET, SOCK_STREAM)
     #    s.bind((host, 1664))
     #    s.listen(5)           
        data = ""
        commandsend = 0
        socks=[s]
	
        while 1:
            if data == "quit":
                run=False
		
                s.close()
                break
	    
            lin, lout, lex=select(socks, [stdin], [],0.5)	    
            for t in lin:
                if t==s: 
                    data = s.recv(1024)
                    conn, addr=s.accept()
                    socks.append(conn)
                    if data:
                        print(data)
                        contenu = data.split('\001')
                        if len(contenu)>1 :
					    	cod = contenu[0]
					    	commande = contenu[1]
					    	contenu_commande = commande.split('#')
						
				
				
							#if cod=='2994' :
				    
			    			if cod=='3994' :
				    			#nouvelle liste sans paranteses
				    			for char in '()':
				        			listNickIPs = commande.replace(char, '')
				        		names = []
				        		ips = []
				        		namesIPs = contenu_commande[1].split(",")
				        		for ni in namesIPs:
							        names.append(ni.split(":")[0])
							    	ips.append(ni.split(":")[1])


				    	    

								#Future dictionnaire
								d = {}
			#On ramplie le dictionnaires a partir de deux listes
			 	    			i = 0
				    			for n in names:
				    				d[n] = ips[i]
					    	        i = i + 1
								# print("voici la liste des personnes connecté : ")
							    #s2 = socket(AF_INET, SOCK_STREAM)
							    #s2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
							    #s2.bind(('127.0.0.1', 1664))
							    #s2.listen(5)
							    #s2.sendto((("2994\001HELLO#")).encode('utf-8'), ('127.0.1.1',1664))
							    #conn, addr = s2.accept()
							    
					    		    
				    			#s2.close()
				    			self.connection =d
				    
				    			for n in self.connection:
				    				print("- "+ n)

							if cod=='4994' :
							    #conn, addr = s.accept()
							    #on envoie un pm
							   	for name in self.connection:
									if(self.connection.get(name)==addr):
										nickname = name
				    			if nickname in self.listban :
				    				print("contenu caché par bannissement")
				    			else:
				    				message = contenu_commande[2]
				    				print(nickname+ " : " +message)
		                    
							if cod=='5994' :
								
								for name in self.connection:
									if self.connection.get(name)==addr :
										nickname = name
				    			if nickname in self.listban :
				    				print("contenu caché par bannissement")
				    			else:
				    				message = contenu_commande[1]
				    				print(nickname+ " : " +message)
			  
                            

		
                   
            for x in lout:
		
				if select([stdin,],[],[],0.0)[0]:
					if x == stdin :
						data = stdin.readline().strip("\n")
			        	#print ("entree clavier : %s" % data) 
				

				
						#lettre = input("Write your message")
						contenu = data.split(' ')


						cod = contenu[0]
						print(cod) 
						if cod=="pm" :
						    codnumber = 4994
						if cod=="bm" :
						    codnumber = 5994
						if cod=="ban" or cod=="unban" :
						    codnumber = 6994
				
				
				    


						if codnumber==4994 :
							nickname = contenu[1]
				    
	     			    	message = contenu[2]
	     			    	for name in self.connection:
				        		if name==nickname :
					    			mess= "4994\001pm#"+nickname+message
					    			s.sendto(mess.encode('utf-8'), self.connection.get(name),1664)
					 #    if codnumber==5994 :
				  #   		#on envoie un bm
				    
				  #   		print(self.connection)
	     #                    message = contenu[1]
				  #   		for name in self.connection:
						# 		print((self.connection.get(name),1664))
						# 		mess = "5994\001bm#"+message
						# 		commandsend = 5994
						# 		print(s)
				  #       		s.sendto(mess.encode('utf-8'), (self.connection.get(name),1664))
					


						# if codnumber == 6994:
	    	# 		    	nikname = contenu[1]
				  #   		print(nikname)
	     #                    if cod == "ban":
	     #                    	self.listban.append(nikname)
	     #                    elif cod == "unban":
	     #                    	self.listban.remove(nikname)
			
	    		
		

		

    def start(self):
        s.sendto(("1994\001START#"+ nickname).encode('utf-8'), (self.address, 1664))

    
                           




if len(argv) == 1:    
    host = gethostbyname(gethostname())
    print (host)
    serveur = Serveur(nickname)
    serveur.genisis(host)
    print(serveur.nom)
    run=True
    while run:
        run=serveur.connexion(run)

       

elif len(argv) == 2:
	host = gethostbyname(gethostname())
    print (host)
    serveur = Serveur(nickname)
    serveur.genisis(host)
    print(serveur.nom)
    run=True
    while run:
        run=serveur.connexion(run)
    client = Client(nickname, argv[1])
    print(argv[1])
    client.connexion(argv[1])
    client.start()
    client.receive()
