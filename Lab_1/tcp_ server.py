import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
#create TCP socket
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind socket to server adress/ port
s_socket.bind((TCP_IP, TCP_PORT))

#listen for incoming connections
s_socket.listen(1)
#accept waits for an upcoming connection

connection, client_adress = s_socket.accept()
print('Connection adress: ', client_adress)
# Receive the data in small chunks and retransmit it
while True:
    data = connection.recv(BUFFER_SIZE)
    if data:
        connection.sendall(data)
    else: break
connection.close()


