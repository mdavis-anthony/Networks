from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(1)

while True:
	print("The server is ready to receive file ...")

	connectionSocket, addr = serverSocket.accept()

	file_data  = connectionSocket.recv(100).decode()

	openedfile = open('server_' + file_data, "wb")

	with openedfile as new_file:

		c = 0

		print('Recieving ' + file_data + ' as server_' + file_data)

		while True:

			file_data  = connectionSocket.recv(1024)

			if not (file_data):

				break
			
			new_file.write(file_data)
			c+= len(file_data)

		print('Total',str(c),'bytes received')

new_file.close()

connectionSocket.close()

	