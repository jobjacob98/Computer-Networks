import socket

s = socket.socket()
s.bind(('172.16.104.64', 2037))
s.listen(1)

n = input("Enter the number of clients: ")

c = []
for i in range(0, n): 
	conn, address = s.accept()
	c.append(conn)

while 1:
	msg = raw_input("Enter msg: ")
	if msg != 'stop': 
		for i in range(0, n):
			c[i].send(msg)
	else:
		for i in range(0, n):
			c[i].send(msg)
		break		

s.close()
