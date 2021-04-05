import socket
from flask import Flask, render_template, jsonify,json, request, url_for

app = Flask(__name__)

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

MULTICAST_TTL = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/_get_data/', methods=['POST'])
def _get_data():
    
    mensaje = request.form
    print(mensaje)
    for key in mensaje.keys():
        data = key
    print(data)
    data_dic = json.loads(data)
    print(data_dic.keys())
    msg = data_dic['message']
    usr = data_dic['user']
    print(usr+": "+msg)
    sock.sendto((usr+": "+msg).encode(), (MCAST_GRP, MCAST_PORT))
    return mensaje
app.run(host='0.0.0.0' ,debug = True)
