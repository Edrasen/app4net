# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:14:33 2020

@author: omar-
"""


import socket
import pickle
import random



def imprime_cuadricula(m, letras):
    raya = '  +' + ('-' * 3 + '+') * 15
    print(raya)
    for i in range(15):
        print(letras[i]+' |', end='')
        for j in range(15):
            if m[i][j]==0:
                m[i][j]=random.choice(letras);
            print('{0:2}'.format(m[i][j]), end=' |')
            if m[i][j]=="":
                m[i][j]=0
        print()
        print(raya) 
      
def main():
    letras=["a","b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024)
        data=pickle.loads(data)
       
        print(data)
     #  """ for i in range(len(data)):
      #      print(data[i])
       # print('Received', data)    """
        m=" "*3
        n=" "*2
        print(" "*4+"0"+m+"1"+m+"2"+m+"3"+m+"4"+m+"5"+m+"6"+m+"7"+m+"8"+m+"9"+n+"10"+n+"11"+n+"12"+n+"13"+n+"14")
    
        imprime_cuadricula(data,letras)
 
    
   
    
main()
