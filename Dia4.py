#Ciclo for -------------------------------------------

# nombres = ["Franklin", "Joan", "Anny","Cynthia","Smirt" ]

# for nombre in nombres:
#     print (f"Bienvenido {nombre}")

# for numero in range (1,10):
#     print (numero)

#Resumen de funciones---------------------------------

# def imprimir (dato):
#     print (dato)

# imprimir("Hola soy una funcion")


# def millasakm (millas):
#     print (millas * 1.6)

# millasakm (2)
# millasakm (2)

# def convetirMillas(kilometros):
#     return kilometros / 1.6

# print (convetirMillas(2))

# def imprimirMenu():
#     print ("------ MENU ------")
#     print ("1- SUMAR ")
#     print ("2- RESTAR")
#     print ("3- MULTIPLICAR")
#     print ("4- DIVIDIR")
#     print ("5- SALIR")


# def sumar ():
#     n1 = int (input ("Ingrese un numero:"))
#     n2 = int (input ("Ingrese otro numero:"))
#     print (f"La suma es:  {n1 + n2}")

# def restar():
#     n1 = int (input ("Ingrese un numero:"))
#     n2 = int (input ("Ingrese otro numero:"))
#     print (f"La resta es: {n1 - n2}")

# def multiplicar():
#     n1 = int (input ("Ingrese un numero:"))
#     n2 = int (input ("Ingrese otro numero:"))
#     print (f"La resta es: {n1 * n2}")

# while True:
#     imprimirMenu()
#     op = input ("Ingrese una opcion: ")

#     if op == "1":
#         sumar()
#     elif op == "2":
#         restar()
#     elif op == "3":
#         multiplicar()
#     elif op == "4":
#         pass
#     elif op == "5":
#         break


numero = 1
suma = 0
contador = 0

while numero != 0:
    numero = int (input ("Ingrese un numero: ") )
    suma = suma + numero
    if numero !=0:
        contador = contador + 1

print (f"Usted ingreso {contador} numeros y la suma de ellos es {suma}")
