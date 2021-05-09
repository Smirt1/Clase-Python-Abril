#OPERACIONES ARITMETICAS

# print("Hola! Dime tu nombre")
# nombre = input()
# print ("Hola, bienvenido")
# print (nombre)

# nombre = input ("Dime tu nombre: ")
# print ("Hola, bienvenido: " + nombre)

# numero_a = int (input ("Indroduzca el primer numero: "))
# numero_b = int (input ("Indroduzca el segundo numero: "))
# suma = (numero_a + numero_b)
# print ("La Sumatoria es :" )
# print (suma)

# numero_a = int (input ("Indroduzca el primer numero: "))
# numero_b = int (input ("Indroduzca el segundo numero: "))
# resta = (numero_a - numero_b)
# print ("La Resta es :" )
# print (resta)

# a = int (input ("Indroduzca el primer numero: "))
# b = int (input ("Indroduzca el segundo numero: "))
# c = int (input ("Indroduzca el tercer numero: "))
# resultado1 = (a+b)*c
# resultado2 = a*c+b*c
# print (resultado1, resultado2 )

# print("Dime el radio")
# radio = int(input())
# pi = 3.14
# longitud = 2 * pi * radio
# print ("Longitud de la circunferencia:")
# print (longitud)

# radio = float (input ("Dime el radio: "))
# pi = 3.14
# longitud = 2 * pi * radio
# print ("Longitud de la circunferencia :", longitud )


# a = float (input ("Indroduzca el primer numero: "))
# b = float (input ("Indroduzca el segundo numero: "))
# suma = (a + b)
# print (suma)


# a = int (input ("Indroduzca el primer numero: "))
# b = int (input ("Indroduzca el segundo numero: "))
# suma = (a + b)
# print ("El resultado de la suma es: ", suma)

a = int (input ("Indroduzca el primer numero: "))
b = int (input ("Indroduzca el segundo numero: "))
resta = (a - b)
print ("El resultado de la resta es: ", resta)

# a = int (input ("Indroduzca el primer numero: "))
# b =  int (input ("Indroduzca el segundo numero: "))
# div = (a // b)
# print ("El resultado de la division es: ", div)

# a = float (input ("Indroduzca el primer numero: "))
# b =  float (input ("Indroduzca el segundo numero: "))
# div = (a / b)
# print ("El resultado de la division es: ", div)


# a = int (input ("Indroduzca el primer numero: "))
# b =  int (input ("Indroduzca el segundo numero: "))
# resi = (a % b)
# print ("El resultado de la division es: ", resi)


# a = float (input ("Indroduzca el primer numero: "))
# b =  float (input ("Indroduzca el segundo numero: "))
# pote = (a ** b)
# print ("El resultado de la division es: ", pote)

# Condicionales if/  for / while: 

# if 2 < 5:
#     print ("2 es menor que 5")

# if 2 > 5:
#     print ("2 es menor que 5")



# edad = int (input ("Cual es su edad? "))

# if edad >= 18:
#      print ("Eres mayor de edad")
# else:
#     print ("Eres menor de edad")

# edad = int (input ("Cual es su edad? "))

#Imprimir un programa que diga si eres mayor o  menor d eedad

# if edad >= 0 and edad <= 17:
#     print ("Eres menor de edad")
# elif edad >= 18 and edad <= 59:
#      print ("Eres mayor de edad")
# else:
#     print ("Eres de la tercera edad")

# Imprimir numeros de 0 a 9

# i = 0

# while i <= 9:
#     print (i)
#     i = i + 1

# Imprimir numeros de 0 a 19

# for i in range (20):
#     print (i)

# Imprimir numeros de 0 a 49

# for y in range (50):
#     print (y)


# x = 0

# while x <= 50:
#     print (x)
#     x = x + 1
    

# Listas

# lista =>[1,2,3,4,5]

# indices        0 1 2 3 4 5 6 7 8 

# lista_numeros = [1,2,3,4,5,6,7,8,9]

# num = lista_numeros[8]
# print (num)

# # cambiar valor en la lista
# lista_numeros[7] = 100
# num = lista_numeros [7]
# print (num)


# print (lista_numeros)

# #agregar valor 22 a la lista
# lista_numeros.append (22)
# print (lista_numeros)

#ver tamanio de lista

# tamanio = len(lista_numeros)
# print (tamanio)

# for numero in lista_numeros:
#     print (numero)
# print ("terminamos de imprimir la lista")

# yo te voy a dar [1,2,3,4,5]
# tu me vas a dar [2,4,6,8,10]

# lista = [1,2,3,4,5]
# lista_nueva = []

# for num in lista:
#     valor_nuevo = num * 2
#     lista_nueva.append(valor_nuevo)

# print (lista_nueva)

#Eliminar varios elementos de una lista

# lista = [1,2,3,4,5,6]
# del lista [3]

# print (lista)


# n = [1, 34, 55, 4, 8]
# x = n [-3:: -1]

# print (x)


#Funciones

# def saludar():
#     print ("Hola a todos!")

# saludar()
# saludar()
# saludar()

# def sumar():
#     print (2+2) 

# sumar()
# sumar()
# sumar()

# def suma_tres_numeros(a, b, c):
#     valor = a + b + c
#     return valor

# suma = suma_tres_numeros (2, 2, 2)
# print (suma)

#Expresiones logicas en python:  == !=  < > >= <= / and or not

# if True:
#     print("Es verdadero")
 

# es_mayor = False
# if es_mayor:
#     print (" Es mayor")
# else:
#     print ("Es menor")

# edad = 11
# es_mayor = edad >= 18
# if es_mayor:
#     print (" Es mayor")
# else:
#     print ("Es menor")

# es_mayor = False
# no_tiene_armas = False

# if es_mayor and no_tiene_armas:
#     print ("Puedes entrar")
# else:
#     print ("No puedes entrar")

