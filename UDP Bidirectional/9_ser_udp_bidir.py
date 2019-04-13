import socket
from threading import Thread

UDP_IP_ADDRESS = "172.16.104.64"
UDP_PORT_NO = 2062

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))	

def receive():
	while True:
		msg, addr = serverSock.recvfrom(1024)
		print msg

def send(ip, port):
	while True:
		msg = raw_input()
		serverSock.sendto(msg, (ip, port))

msg, addr = serverSock.recvfrom(1024)

t1 = Thread(target=receive)
t2 = Thread(target=send, args=(addr))

t1.start()
t2.start()
