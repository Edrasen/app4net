import socket
import rpyc
import struct
from threading import Thread
from rpyc.utils.server import ThreadedServer

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
user_list = ["Todos"]
#recived_list = []

exit_msg = " ha dejado el chat."
join_msg = " se ha unido al chat."

def com():
    print("Server started...\nWaiting for connections...\n")
    while True:
        sender = ""
        reciver = ""
        recived, addres = sock.recvfrom(10240)
        recived = recived.decode()
        print(recived)
        limit_sender = recived.find(":")
        limit_reciver = recived.find("+")
        sender = recived[:limit_sender]
        reciver = recived[limit_reciver+1:]
        usuarios[sender] = addres
        print(usuarios)
        
        if recived[limit_sender+1:limit_reciver] == " {quit}":
            usuarios.pop(sender)
            user_list.remove(sender)

        for elem in usuarios: 
            if recived[limit_sender+1:limit_reciver] == " {quit}":
                sock.sendto((sender+exit_msg).encode(), usuarios[elem])
            elif recived[limit_sender+1:limit_reciver] == " {hi}":
                if recived[:limit_sender] not in user_list:
                    user_list.append(sender)       #adding a list of users
                sock.sendto((sender+join_msg).encode(), usuarios[elem])
            else:
                if reciver == "Todos":
                    sock.sendto(recived[:limit_reciver].encode(), usuarios[elem])
                elif elem == reciver:
                    sock.sendto(recived[:limit_reciver].encode(), usuarios[reciver])
                    sock.sendto(recived[:limit_reciver].encode(), usuarios[sender])

class users_list(rpyc.Service):
    def exposed_list_clients(self):
        return user_list

server = ThreadedServer(users_list, port = 1235)
ACCEPT_THREAD = Thread(target=com)
ACCEPT_THREAD.start()
server.start()
sock.close()
