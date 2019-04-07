import socket

msg = "Hi There!!"

s = socket.socket()
s.bind(('172.16.104.64', 2023))
s.listen(1)

c, addr = s.accept()

#print(c, "\n", addr)

c.send(msg)

s.close()
