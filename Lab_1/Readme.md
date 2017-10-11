# Laboratory work nr 1
---
### Objectives 
Get to remember (or learn and understand) what you did at the Programarea în Rețea course:

* build TCP and UDP server/client "programs" using sockets;
* get an HTTP page (read RFC 2616);
* I had fun
---
### Task 1: send UDP and TCP messages

---
### Task 1.1 send a message at fixed intervals

---
### Task 2: port scanning of a given IP

Generally speaking port scanning is the process of checking whether a port is avaliable or not. For example, suppose we have a city full of buildings. Each building has more appartments. If we relate to this example, then every builing has an adress which in our case is the IP adress. Then every building has more appartments(we can associate appartments with ports in our case.) Having all these associations in mind, a port scaning is actually the process when a person is checking all the doors of a building: are they open or not? 

So, in order to be able to scan ports one should: 
* specify the IP adress or the hostname 
* indicate the range of ports to scan (there are 0..65535 ports)
* TCP connect() in order to open a connection to every interesting port on the machine (in case of TCP connection)
* The port is reached/avaliable in case the port is listening to the previous action( successfully open a conection using the connect() system call provided by an OS)

So, to sum it up, the pseudo-code, could look like this: 
~~~
#this is done through sockets
import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'utm.md'
#now define the port ranges, define x as the nr of the port
for x in range(100):
  s.connect((server, x))
  #if connection is made return True
  #otherwise return False
~~~

It's important to notice that there are different types of techniques used in order to do port scanning. The one described above can be slow, taking into consideration that there are more than 65000 ports to be scanned. 


There are two general use cases of ports scanning: 
* Administrators - using it in order to test a system and assure that it's working properly and no breaks of the system will appear
* Attackers use to discover services they can break into

---
### References 
[https://pymotw.com/2/socket/tcp.html](https://pymotw.com/2/socket/tcp.html)
[https://wiki.python.org/moin/TcpCommunication](https://wiki.python.org/moin/TcpCommunication)
[https://wiki.python.org/moin/UdpCommunication](https://wiki.python.org/moin/UdpCommunication)
