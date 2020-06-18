from math import *
import basics

names = {'sqrt': sqrt, 'sin': sin, "cos": cos, "tan": tan, "log":log}
operadores = "+*^/()-"   

def evaluacionPosfija(expresionPosfija):
    pilaOperandos = []
    listaSimbolos = expresionPosfija.split()
    for simbolo in listaSimbolos:
        if simbolo.isnumeric():
            pilaOperandos.append(int(simbolo))
        elif simbolo in operadores:
            operando2 = pilaOperandos.pop()
            operando1 = pilaOperandos.pop()
            resultado = basics.calculate(simbolo,operando1,operando2)
            pilaOperandos.append(resultado)
        else:
            pilaOperandos.append(eval(simbolo))
    return pilaOperandos.pop()

################################### EVALUA LA EXPRESION EN NOTACION PREFIJA #########################################
def evaluacionPrefija(expresionPrefija):
    pilaOperandos = []
    expresionPrefija_inversa = expresionPrefija[::-1]
    listaSimbolos = expresionPrefija_inversa.split()
    for simbolo in listaSimbolos:
        if simbolo.isnumeric():
            simbolo = str(simbolo[::-1])
            pilaOperandos.append(int(simbolo))
        elif simbolo in operadores:
            operando1 = pilaOperandos.pop()
            operando2 = pilaOperandos.pop()
            resultado = basics.calculate(simbolo, operando1, operando2)
            pilaOperandos.append(resultado)
        else:
            simbolo = simbolo[::-1]
            pilaOperandos.append(eval(simbolo))
    return  pilaOperandos.pop()

##################################### CONVIERTE LA CADENA DE INFIJA A POSFIJA ######################################
def infija_a_Posfija(expresionInfija):
    precedencia = {}
    precedencia["^"] = 4
    precedencia["*"] = 3
    precedencia["/"] = 3
    precedencia["+"] = 2
    precedencia["-"] = 2
    precedencia["("] = 1
    pilaOperadores = []
    listaPosfija = []
    listaSimbolos = expresionInfija.split()
    for simbolo in listaSimbolos:
        if simbolo.isnumeric():
            listaPosfija.append(simbolo)
        elif simbolo == '(':
            pilaOperadores.append(simbolo)
        elif simbolo == ')':
            simboloTope = pilaOperadores.pop()
            while simboloTope != '(':
                listaPosfija.append(simboloTope)
                simboloTope = pilaOperadores.pop()
        elif simbolo in operadores:
            while pilaOperadores and \
            (precedencia[pilaOperadores[len(pilaOperadores)-1]] >= \
                precedencia[simbolo]):
                listaPosfija.append(pilaOperadores.pop())
            pilaOperadores.append(simbolo)
        else:
            listaPosfija.append(str(eval(simbolo)))
    while pilaOperadores:
        listaPosfija.append(pilaOperadores.pop())
    return " ".join(listaPosfija)

def evaluacionInfija(expresionInfija):
    posfija = infija_a_Posfija(expresionInfija)
    res = evaluacionPosfija(posfija)
    return res
