#!/usr/bin/python
from socket import *
from select import select

def main():
	
	class Chat_Server():
		def run():
			HOST = ''
			PORT = 1664
			s = socket(AF_INET, SOCK_STREAM)
			s.bind(('0.0.0.0', 1664))
			s.listen(5)
			socks=[s]
			while True:
				lin, lout, lex=select(socks,[],[])
				print "select got %d read events" % (len(lin))
				for t in lin:
					if t==s:
						(c,addr)=s.accept()
						msg="Bienvenue dans le chat %s\n" % (addr[0],)
						print msg
						socks.append(c)
						c.send(msg) #à envoyer en broadcast 
					else:
						who=t.getpeername()[0]
						data=t.recv(1024)
						
