import rpyc

c = rpyc.connect('localhost', 12345)

flag = 1

while flag == 1:
    print("\t\t\tBienvenido a RPC_calculator! :)\t\t\t\n")
    mode = int(input("Seleccione la notación que va a utilizar: \n1.Prefija \n2.Infija \n3.Posfija \n4.Salir \n"))
    if mode == 1:
        try:
            expresion = input("Introduzca la expresión prefija a evaluar: \n")
            res = c.root.prefija(expresion)
            print("Resultado: ", res)
        except:
            print("\n\t\tError en la expresión\t\t\n")
    elif mode == 2:
        try:
            expresion = input("Introduzca la expresión infija a evaluar: \n")
            res = c.root.infija(expresion)
            print("Resultado: ", res)
        except:
            print("\n\t\tError en la expresión\t\t\n")
    elif mode == 3:
        try:
            expresion = input("Introduzca la expresión posfija a evaluar: \n")
            res = c.root.posfija(expresion)
            print("Resultado: ", res)
        except:
            print("\n\t\tError en la expresión\t\t\n")
    elif mode == 4:
        break
    