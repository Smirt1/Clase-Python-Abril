def imprimirMenu():
    print ("------ MENU ------")
    print ("1- SUMAR ")
    print ("2- RESTAR")
    print ("3- MULTIPLICAR")
    print ("4- DIVIDIR")
    print ("5- SALIR")


def sumar ():
    n1 = int (input ("Ingrese un numero:"))
    n2 = int (input ("Ingrese otro numero:"))
    print (f"La suma es:  {n1 + n2}")

def restar():
    n1 = int (input ("Ingrese un numero:"))
    n2 = int (input ("Ingrese otro numero:"))
    print (f"La resta es: {n1 - n2}")

def multiplicar():
    n1 = int (input ("Ingrese un numero:"))
    n2 = int (input ("Ingrese otro numero:"))
    print (f"La resta es: {n1 * n2}")

while True:
    imprimirMenu()
    op = input ("Ingrese una opcion: ")

    if op == "1":
        sumar()
    elif op == "2":
        restar()
    elif op == "3":
        multiplicar()
    elif op == "4":
        pass
    elif op == "5":
        break