import socket
import struct
from threading import Thread

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
IS_ALL_GROUPS = True

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if IS_ALL_GROUPS:
    # on this port, receives ALL multicast groups
    sock.bind((MCAST_GRP, MCAST_PORT))
else:
    # on this port, listen ONLY to MCAST_GRP
    sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

usuarios = {}
recived_list = []

exit_msg = " ha dejado el chat."

def com():
    while True:
        recived, addres = sock.recvfrom(10240)
        recived = recived.decode()
        print(recived)
        limit = recived.find(":")
        usuarios[recived[:limit]] = addres
        print(usuarios)
        
        if recived[limit+1:] == " {quit}":
            usuarios.pop(recived[:limit])

        for elem in usuarios: 
            #if(addres != usuarios[elem]):
            if recived[limit+1:] == " {quit}":
                sock.sendto((recived[:limit]+exit_msg).encode(), usuarios[elem])
            else:
                sock.sendto(recived.encode(), usuarios[elem])

ACCEPT_THREAD = Thread(target=com)
ACCEPT_THREAD.start()
ACCEPT_THREAD.join()
sock.close()
