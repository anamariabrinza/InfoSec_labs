#client
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = 'Buna, Ana-Maria'

c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the socket to the port where the server is listening
c_sock.connect((TCP_IP,TCP_PORT))
#connection is established
c_sock.send(MESSAGE.encode('utf-8'))
data = c_sock.recv(BUFFER_SIZE)

c_sock.close()

print('Received data: ', data)
