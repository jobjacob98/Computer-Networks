import socket

c = socket.socket()

c.connect(('172.16.104.64', 2037))

while 1:
	count = c.recv(1000)
	if count != 'stop':
		print count
	else:
		break

c.close()
