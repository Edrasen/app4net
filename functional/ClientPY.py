import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1234        # The port used by the server

def conn():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        option = input("Selecciona la dificultad: \n")
        optsel = option +"\r"
        s.sendall(optsel.encode())
        data = s.recv(1024)
        word = data.decode('UTF-8')
        #print("Recibido: " + word)
        #print(word)
    return word

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
    word  = conn()
    wordad = word[0:len(word)-2]
    hidden = showLines(wordad)
    print("".join(hidden))
    intentos = len(word)+2
    if intentos >= 8:
        intentos = int(intentos/1.2)
    for i in range(intentos):
        if("".join(hidden) == wordad):
            print("\nJUEGO TERMINADO\n")
            print("HAZ GANADO :)!!!!!")
            res = "VICTORIA\r"
            break
        buscar = input("Introduzca la letra que cree que completa la palabra: \n")
        print("Le quedan "+ str(intentos-1-i) + " intentos")
        search(buscar, word, hidden)
        print("".join(hidden))
        if intentos-i == 1:
            print("\nJUEGO TERMINADO\n")
            print("Haz perdido :(")

play()
