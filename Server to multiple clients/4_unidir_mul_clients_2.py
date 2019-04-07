import socket

c = socket.socket()

c.connect(('172.16.104.64', 2037))

while 1:
	msg = c.recv(1000)
	if msg != 'stop':
		print msg
	else:
		break

c.close()
