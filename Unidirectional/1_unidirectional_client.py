import socket

c = socket.socket()

c.connect(('172.16.104.64', 2023))

msg = c.recv(1000)
print msg

c.close()

