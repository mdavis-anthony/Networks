from socket import *

server = 'localhost'

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((server,serverPort))

file = input('Please input the filename to be sent to the server:')

print('Starting to send ' + str(file))

file_name = clientSocket.send(file.encode())

openedfile = open(file, "rb")

file_size = open(file, "rb").seek(0,2)

file_size = open(file, "rb").tell()

bsent = 0

with openedfile as sent_file:

	c = 0 

	read = openedfile.read()

	while c <= file_size:

		if not read:

			break

		bytes_sent = clientSocket.send(read)

		bsent += bytes_sent

		c+= len(read)

print('Total ' + str(bsent) + ' bytes sent')

openedfile.close()

clientSocket.close()
