import base64
import socket

def main():
	max_size = 10240
	IP_addr = socket.gethostbyname(socket.gethostname())
	port_no = 2000	
	client_sock = connect_to_server(IP_addr, port_no)
	while 1:
		show_menu()
		ch = input()
		if ch == 1:
			client_sock.sendto(str(ch), (IP_addr, port_no))
			recv_list, addr = client_sock.recvfrom(1024)
			print recv_list
		elif ch == 2: 
			img_name = raw_input("\nEnter the image name: ")
			client_sock.sendto(img_name, (IP_addr, port_no))
			recv_data, addr = client_sock.recvfrom(max_size)
			img_flag, img = check_img(recv_data)
			if img_flag == 1:
				save_ch = raw_input("\nImage received. The image will be saved in the client_images directory. Do you want to save it in a different path? (y/n): ")
				if save_ch == 'y':
					img_path = raw_input("\nEnter the path: ")
				else:
					img_path = "client_images/" + img_name
				with open(img_path, "wb") as img_file:
					img_file.write(img)
				print "\nImage saved successfully!!\n"
			elif img_flag == 0:
				print recv_data
		elif ch == 3:
			client_sock.sendto("stop", (IP_addr, port_no))
			print "\n\nExiting...\n"
			break
		else:
			print "\nSorry...wrong choice. Please try again!\n"

def connect_to_server(IP_addr, port_no):			
	client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client_sock.sendto("check", (IP_addr, port_no))
	print "\nChecking for server... (if the program is hung on this message, kindly turn on the server and try again!!)"
	recv_msg, addr = client_sock.recvfrom(1024)
	print "\nConnected to server at " + str(IP_addr) + "/" + str(port_no) + "\n"	
	return client_sock

def show_menu():
	print "Enter 1 for getting a list of images in server"
	print "Enter 2 to get an image from server"
	print "Enter 3 to exit"

def check_img(recv_data):
	try:
		img = base64.b64decode(recv_data)
		return 1, img
	except:
		return 0, None


if __name__ == '__main__' :
	main()
