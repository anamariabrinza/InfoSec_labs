#SERVER
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

#create an INET, STREAMing socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind the socket to a public host,
# and a well-known port
server_sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = server_sock.recvfrom(1024) #buffer size
    print("received message:", data)