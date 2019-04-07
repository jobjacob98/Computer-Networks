import socket

s = socket.socket()
s.bind(('172.16.104.64', 2037))
s.listen(1)

c, addr = s.accept()

i = 0

while 1:
	string = raw_input("Enter the string: ")
	sub_string = raw_input("Enter the substring: ")

	len_sub = len(sub_string)

	count = 0
	i = 0
	while i+len_sub <= len(string):
		k = 0
		j = i
		while k < len_sub:
			if string[j] == sub_string[k]:
				flag = 1
				k += 1
				j += 1
			else:
				flag = 0
				break
		if flag == 1:
			count += 1
		i += 1

	c.send(str(count))	
	ch = raw_input("Do you want to continue? (y/n): ")
	if ch == 'n':
		c.send('stop')
		break
	
s.close()
