import base64
import socket
import os

def main():
	max_size = 10240
	IP_addr = socket.gethostbyname(socket.gethostname())
	port_no = 2000	
	server_sock = start_server(IP_addr, port_no)
	addr = establish_connection(server_sock)
	while True:
		req, addr = server_sock.recvfrom(1024)
		if req == '1':
			imgs_path = "server_images/"
			imgs = os.listdir(imgs_path)			
			list_data = "\nImages available:\n"
			for img in imgs:
				img_size = os.path.getsize(imgs_path+img)
				list_data += img + " (" + str(img_size/1024) + "kB)\n"
			list_data += "\n"
			server_sock.sendto(list_data, addr)
		elif req == "stop":
			print "\nClient dissconnected..."
			break			
		else:
			req_img = "server_images/" + req	
			exists = os.path.isfile(req_img)
			if exists:
				img_size = os.path.getsize(req_img)
				if img_size < max_size:
					with open(str(req_img), "rb") as img_file:
						img_str = base64.encodestring(img_file.read())
					server_sock.sendto(img_str, addr)
				else: 
					size_msg = "\nSorry...you can only request images that are less than 10kB.\n"
					server_sock.sendto(size_msg, addr)	
			else:
				not_found_msg = "\nThe requested image is not found!!\n"
				server_sock.sendto(not_found_msg, addr)	
	print "\nExiting...\n"

def start_server(IP_addr, port_no):	
	server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_sock.bind((IP_addr, port_no))
	print "\nServer started at " + str(IP_addr) + "/" + str(port_no) + "\n"
	return server_sock

def establish_connection(server_sock):
	check_msg, addr = server_sock.recvfrom(1024)
	server_sock.sendto("connected", addr)
	print "Connection with client established!!\n"
	return addr


if __name__ == '__main__' :
	main()
