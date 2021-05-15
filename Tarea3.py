# 1- Hacer una función que potencie un número x a la y

def potenciar(a, b):
    print (a * b)

potenciar(4,4)


# 2- Realizar una función que pida por pantalla un número del 1 al 10 y muestre
# por pantalla el número escrito en letras.


# def numeros_a_letras():
#     n = int(input("Dame un número del 1 al 10: "))

#     if n > 10:
#         print(" Te pedí un numero del 1 al 10")
#     elif n == 1:
#         print("Uno")
#     elif n == 2:
#         print("Dos")
#     elif n == 3:
#         print("Tres")
#     elif n == 4:
#         print("Cuatro")
#     elif n == 5:
#         print("Cinco")
#     elif n == 6:
#         print("Seis")
#     elif n == 7:
#         print("Siete")
#     elif n == 8:
#         print("Ocho")
#     elif n == 9:
#         print("Nueve")
#     elif n == 10:
#         print("Diez")

# numeros_a_letras()


# 3- Hacer una función que reciba un año como argumento y retorne
# verdadero si es bisiesto.

# def ano_bisiesto(a):
#     if a % 4 == 0:
#         if a % 100 == 0:
#             if a % 400 == 0:
#                 print(True)
#             else:
#                 print(False)
#         else:
#             print(True)
#     else:
#         print(False)

# ano_bisiesto(1984)
# ano_bisiesto(2000)

# 4- Crear una función que evalúe dos números y retorne verdadero si ambos
# números son iguales.

# def soniguales(x, y):
#     if x == y:
#         print(True)
#     else:
#         print(False)

# soniguales(2,2)
# soniguales(2,1)


# 5- Un número palindrómico se lee igual en ambos sentidos. El palíndromo más
# grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.
# Cree una función que encuentre el palíndromo más grande hecho del
# producto de dos números de 3 dígitos.


# 6- Hacer una función que reciba una cedula como argumento y diga si la
# cedula es válida o no.

# def comparador_cedulas():
#     cedula = input("Introduzca la cedula a comprobar sin guiones: ")

#     if len(cedula) > 11:
#         print("Cédula incorrecta")
#     else:
#         print("Cédula válida")

# comparador_cedulas()


# 7- Hacer una función que reciba como argumento una lista de elementos
# numéricos y retorno otra lista con cada elemento de la primera lista
# duplicados.


# 8- Hacer una función que reciba un valor iniciar y uno final, y muestre en
# pantalla las tablas de multiplicar de los números múltiplos de 6 que hay
# entre el valor inicial y el valor final.

# def tabla_multiplicar_num4(v_inicial, v_final):
#     n = 4 

#     if v_inicial > v_final:
#         print("Error: Valor Inicial debe ser menor al Valor Final")
#     else:
#         while v_inicial <= v_final:
#             res =  n * v_inicial
#             print(f"{n} X {v_inicial} = {res}")
#             v_inicial += 1


# tabla_multiplicar_num4(6, 20)
