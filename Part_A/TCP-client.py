from socket import *
server  = 'localhost'

serverPort =12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((server,serverPort))

sentence = input('Input lowercase sentence:')

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print('From Server: ', modifiedSentence.decode())

clientSocket.close()