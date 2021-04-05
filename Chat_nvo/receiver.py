import socket
import struct
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chat-b5825.firebaseio.com/'
})
ref = db.reference('chat')

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

while True:
  
    recived, addres = sock.recvfrom(10240)
    recived = recived.decode()
    print(recived)
    limit = recived.find(":")
    usuarios[recived[:limit]] = addres
    print(usuarios)
    ref.push({
        'user': recived[:limit],
        'txt': recived[limit+1:]
        })  
    
    if recived[limit+1:] == " salir":
        usuarios.pop(recived[:limit])

    for elem in usuarios: 
        if(addres != usuarios[elem]):
            sock.sendto(recived.encode(), usuarios[elem])


