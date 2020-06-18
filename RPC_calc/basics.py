def multi(operandoIzquierda, operandoDerecha):
    return operandoIzquierda * operandoDerecha

def div(operandoIzquierda, operandoDerecha):
    return operandoIzquierda / operandoDerecha

def suma(operandoIzquierda, operandoDerecha):
    return operandoIzquierda + operandoDerecha

def resta(operandoIzquierda, operandoDerecha):
    return operandoIzquierda - operandoDerecha

def pot(operandoIzquierda, operandoDerecha):
    return operandoIzquierda ** operandoDerecha

def calculate(operador, operandoIzquierda, operandoDerecha):
    if operador == "*":
        return multi(operandoIzquierda, operandoDerecha)
    elif operador == "/":
        return div(operandoIzquierda,operandoDerecha)
    elif operador == "+":
        return suma(operandoIzquierda,operandoDerecha)
    elif operador  == "-":
        return resta(operandoIzquierda, operandoDerecha)
    elif operador == "^":
        return pot(operandoIzquierda, operandoDerecha)
