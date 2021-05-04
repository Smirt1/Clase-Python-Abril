
#Escriba en pantalla el tipo de dato que retorna la expresión 4 < 2:

# print (4 < 2)

#Almacene en una variable el nombre de una persona y al final muestre en la consola el me nsaje: “Bienvenido [nombrePersona]”

# usuario = input("Escriba el nombre del usuario: ")
# print ("Bienvenido : " + usuario)

#Evalúe si un número es par o impar y muestre en la consola el mensaje.

# numero =  int (input("Escriba el numero: "))
# print (numero % 2)

#Almacene dos números y evalúe si el primero es mayor que el segundo. El resultado debe verse en la consola.

# numero_a = 2
# numero_b = 4
# resultado = (numero_a > numero_b)
# print (resultado)

#Convierta dólares a pesos.

# cantidad_dolares = 89.75
# tasa = 58.50
# print (cantidad_dolares * tasa)


# Convierta grados celsius a Fahrenheit

# grados_celcius = int(input ( "Intruzca la temperatura a convertir: "))
# print (grados_celcius * 1.8 + 32)

# Almacene cuatro notas 90,95,77, 92 y las promedie. Al final debe decir su calificación en letras A, B,C,D, E ó F.

nota_1 = 90
nota_2 = 95
nota_3 = 90
nota_4 = 92

promedio = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print (promedio)

if promedio >= 90 and promedio <= 100:
    print("Su nota es A")
elif promedio >= 80 and promedio <= 89:
    print ("Su nota es B")
elif promedio >= 70 and promedio <= 79:
    print("Su nota es C")
elif promedio >= 60 and promedio <= 69:
    print("Su nota es D")
elif promedio >= 50 and promedio <= 59:
    print("Su nota es E")
else:
    print("Su nota es F")

#Que almacene monto, cantidad de cuotas, y porcentaje de interés anual de un préstamo y calcule la cuota mensual. (Amortizar mediante el sistema francés)


# prestamo = float (input ("Ingrese el valor del prestamo: "))
# interes = float (input ("Ingrese la tasa solicitada:"))
# cuotas = int(input ("Ingrese el tiempo a pagar:"))



