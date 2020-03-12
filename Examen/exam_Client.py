# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:14:33 2020

@author: omar-
"""

import socket
import pickle
import random



def imprime_cuadricula(m, letras):
    cont=0
    raya = '   +' + ('-' * 3 + '+') * 15
    print(raya)
    separacion=' |'
    for i in range(15):
        if i>9:
            separacion='|'
        print(cont,separacion , end='')
        for j in range(15):
            if m[i][j]==0:
                m[i][j]=random.choice(letras);
            print('{0:2}'.format(m[i][j]), end=' |')
            if m[i][j]=="":
                m[i][j]=0
        cont+=1
        print()
        print(raya) 
def encuentraPal(palabras, posiciones, coordenada):
    n=0
    palabra=""
    for i in posiciones:
        if coordenada==i:
            posiciones.pop(n)
            
            palabra= palabras.pop(n)
            break
        n+=1
    print(n, coordenada)
    return palabra, posiciones, palabras
    

def concepto(posicionesNuevo,palabra,Matriz,letras):
    encontro=False
    m=" "*3
    n=" "*2
    while len(posicionesNuevo) >0:
        print("\nEncontrar la siguiente lista de palabras: \n\n",palabra,"\n")
        print(" "*4+"0"+m+"1"+m+"2"+m+"3"+m+"4"+m+"5"+m+"6"+m+"7"+m+"8"+m+"9"+n+"10"+n+"11"+n+"12"+n+"13"+n+"14")
        imprime_cuadricula(Matriz,letras)
        renglon1=int(input("¿Encontraste una palabra? \nColoca el renglon de su inicial: "))
        columna1=int(input(" Coloca la columna de su inicial: "))
        renglon2=int(input("Ahora Coloca el renglon de donde termina: "))        
        columna2=int(input(" Coloca la columna de donde termina: "))
        for i in posicionesNuevo:
            if i is not None and i!=[]:
                if renglon1==i[0] and columna1==i[1] and renglon2==i[2] and columna2==i[3]:
                    pal,posicionesNuevo,palabra=encuentraPal(palabra, posicionesNuevo,i)
                    print("Encontraste ",pal)
                    encontro=True
        if encontro==False:
            print("Te equivocaste, intentalo denuevo")
        encontro=False
    print("FELICIDADES ENCONTRASTE LAS PALABRAS")
    
def main():
    letras=["a","b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024)
        data2=s.recv(1024)
        palabra= s.recv(1024)
        
        Matriz=pickle.loads(data)
        posiciones=pickle.loads(data2)
        palabra=pickle.loads(palabra)
        for i in data2:
            if i==None or i==[]:
                data2.remove(i)
        
        posicionesNuevo=[]
        for i in posiciones:
            if i!=None and i!=[]:
                posicionesNuevo.append(i)
        print(posicionesNuevo)
        print("\n\n\n\n\n\t\t\t----------------------------------")
        print("\t\t\t|¿Qué categoria quieres jugar?      |")
        print("\t\t\t----------------------------------")
        print("\t\t\tA) CONCEPTO\n\t\t\tB) ANAGRAMA")
        opcion=input("\t\t\tSelecciona una opcion:" )
        if opcion in "Aa":
            concepto(posicionesNuevo, palabra, Matriz,letras)
        if opcion in "Bb":
            concepto(posicionesNuevo, palabra, Matriz,letras)
     #  """ for i in range(len(data)):
      #      print(data[i])
       # print('Received', data)    """
       
   
    
main()