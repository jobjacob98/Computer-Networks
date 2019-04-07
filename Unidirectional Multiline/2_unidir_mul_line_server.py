import socket

s = socket.socket()
s.bind(('172.16.104.64', 2035))
s.listen(1)

c, addr = s.accept()

while 1:
	msg = raw_input("Enter msg: ")
	if msg != 'stop': 
		c.send(msg)
	else:
		c.send(msg)
		break		

s.close()
