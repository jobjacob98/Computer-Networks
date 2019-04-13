import socket
from threading import Thread

UDP_IP_ADDRESS = "172.16.104.64"
UDP_PORT_NO = 2062

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive():
	while True:
		msg, addr = clientSock.recvfrom(1024)
		print msg

def send():
	while True:
		msg = raw_input()
		clientSock.sendto(msg, (UDP_IP_ADDRESS, UDP_PORT_NO))

clientSock.sendto("start", (UDP_IP_ADDRESS, UDP_PORT_NO))

t1 = Thread(target=receive)
t2 = Thread(target=send)

t1.start()
t2.start()
