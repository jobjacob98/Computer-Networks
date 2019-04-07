import socket
from threading import Thread

def send():
	while 1:
		msg = raw_input()
		if msg != 'stop': 
			c.send(msg)
		else:
			c.send(msg)
			break		
	s.close()

def receive():
	while 1:
		msg = c.recv(1000)
		if msg != 'stop':
			print msg
		else:
			break
	s.close()

s = socket.socket()
s.bind(('172.16.104.64', 2116))
s.listen(1)
c, addr = s.accept()

t1 = Thread(target=send)
t2 = Thread(target=receive)

t1.start()
t2.start()
	
