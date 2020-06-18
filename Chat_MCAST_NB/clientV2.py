import socket
from threading import Thread
class sender:
    mcast_g = ""
    mcast_pt = 0
    mcast_ttl = 0

    def __init__(self, mcast_g, mcast_pt, mcas_ttl):
        self.mcast_g = mcast_g
        self.mcast_pt = mcast_pt
        self.mcast_ttl = mcas_ttl
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, self.mcast_ttl)
        #self.name = input("Escribe tu nombre: ")
        #print("Welcome ", self.name)
