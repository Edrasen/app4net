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
    
    def enviar(self, msg, name):
        #while True:
            #mensaje = input(name + ": ")
            self.sock.sendto((name +": "+msg).encode(), (self.mcast_g, self.mcast_pt))
            
    
    def recibir(self):
        while True:
            recived = self.sock.recv(10240).decode()
            #print(recived)

    def comunicar(self):
        #thread_send = Thread(target=self.enviar)
        thread_recv = Thread(target=self.recibir)

        #thread_send.start()
        thread_recv.start()

        #thread_send.join()
        thread_recv.join()

    