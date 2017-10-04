#CLIENT
import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005 #real time transport protocol
MESSAGE = "Buna dimineata, Ana-Maria"
max_n = 4
'''
print('UDP target IP: ', UDP_IP)
print('UDP target port: ', UDP_PORT)
print("message: ", MESSAGE)
'''
#create an INET, STREAMing socket
client_sock = socket.socket(socket.AF_INET, #internet
                        socket.SOCK_DGRAM) #UDP
#for and time-out
for i in range(max_n):
    time.sleep(5)
    client_sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))