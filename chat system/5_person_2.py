import socket
from threading import Thread

def send():
	while 1:
		msg = raw_input()
		if msg != 'stop': 
			s.send(msg)
		else:
			s.send(msg)
			break		
	s.close()

def receive():
	while 1:
		msg = s.recv(1000)
		if msg != 'stop':
			print msg
		else:
			break
	s.close()

s = socket.socket()
s.connect(('172.16.104.64', 2116))

t1 = Thread(target=send)
t2 = Thread(target=receive)

t1.start()
t2.start()


