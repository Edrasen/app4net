from time import time
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1234        # The port used by the server


def showLines(word):
    hidden = []
    print("La palabra tiene: " +str(len(word))+ " letras") 
    for letra in word:
        hidden.append(" _")
    #print(hidden)
    return hidden

def search(letra, word, hidden):
    lword = list(word)
    for i in range(len(word)):
        if letra ==  lword[i]:
            hidden[i] = letra
    return hidden

def play():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        option = input("Selecciona la dificultad: \n")
        optsel = option +"\r"
        s.sendall(optsel.encode())
        data = s.recv(1024)
        word = data.decode('UTF-8')
        res,scr = playgame(word, option)
        scr = int(scr)
        stscr = str(scr) +"\r"
        s.sendall(res.encode())
        s.sendall(stscr.encode())
        #print("Recibido: " + word)
        print(stscr)
        #print(word)
        s.close()
            
def playgame(word, option):
        score = 0
        word = word[:len(word)-1]
        hidden = showLines(word)
        print("".join(hidden))
        intentos = len(word)+3
        if intentos >= 9:
            intentos = int(intentos/1.2)
        start_time = time()
        for i in range(intentos):
            if("".join(hidden) == word):
                print("\nJUEGO TERMINADO\n")
                print("HAZ GANADO :)!!!!!")
                res = "VICTORIA\r"
                elapsed_time = time() - start_time
                score = 0
                if option == '1':
                    score = elapsed_time/1
                elif option == '2':
                    score = elapsed_time/1.2
                else:
                    score = elapsed_time/1.3

                print("Elapsed time: %d seconds." % elapsed_time)
                print("Score: %d" % score)
                break
            buscar = input("Introduzca la letra que cree que completa la palabra: \n")
            print("Le quedan "+ str(intentos-1-i) + " intentos")
            search(buscar, word, hidden)
            print("".join(hidden))
            if intentos-i == 1:
                print("\nJUEGO TERMINADO\n")
                print("HAZ PERDIDO :(")
                res = "DERROTA\r"
                score = 0        
        return res, score

play()
