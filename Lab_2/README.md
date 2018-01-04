# Laboratory work nr 4

## Objectives
Learn how to use the network as an attack vector. Impliment one of the following: TCP SYN flood, HTTP Slowloris or HTTP slow POST

## Implementation 

In this work I tried to implement the TCP SYN Flood attack. 
This attack is based on ”three-way handshake”. A client sends a TCP SYN (S flag) packet to begin a connection to the server. The target server replies with a TCP SYN-ACK (SA flag) packet, but the client does not respond to the SYN-ACK, leaving the TCP connection “half-open”. In normal operation, the client should send an ACK (a flag) packet followed by the data to be transferred, or an RST reply to reset the connection. On the target server, the connection is kept open, in a “SYN_RECV” state, as the ACK packet may have been lost due to network problems.

The main purpose is to open as many as possible half-connections to the target server. Once the server is full of half-open TCP connections it will stop working properlly. 

In order to simulate a DDoS, I generated SYN flood packets with Scapy(which is very powerful and facilitates a lot the whole process).

The target server is on my virtual machine and it is an Apache server on Ubuntu server. 

The next image illustrates the ubuntu server on virtual machine and the target ip adress can be seen from the image.
![](http://i63.tinypic.com/5l4avc.png)

The sourse ip adress is my server/computer. And if we try to check the conection between these two, it works. The same can be seen in the next image:
![](http://i64.tinypic.com/scxk6b.png)

Then after we ran the attack we can check the usage of CPU/Memory of the 
server using the HTOP comand, and in the image is what we get before and after. 
![](http://i68.tinypic.com/20f3jab.png)
