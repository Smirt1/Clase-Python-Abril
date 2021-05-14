
# 1 – Realizar un programa que solicite al usuario un número indeterminado de
# números (mientras se tecleen números que no sean cero). Al salir el programa
# debe dar en pantalla el total de números dados y la suma de ellos.


# numero = 1
# suma = 0
# contador = 0

# while numero != 0:
#     numero = int (input ("Ingrese un numero") )
#     suma = suma + numero
#     if numero !=0:
#         contador = contador + 1

# print (f"Usted ingreso {contador} numeros y la suma de ellos es {suma}")



# 2- Realizar un programa que presente un menú con las siguientes opciones
#   Convertir grados a Celsius a Fahrenheit
#   Convertir dólar a pesos
#   Convertir metros a pies
#   Salir

# print (" Seleccione una opcion!!!!: \n 1-Convertir de grados Celcius a Fahrenheit \n 2-Convertir dólar a pesos\n 3-Convertir metros a pies \n Presione cualquier tecla para salir.")

# opcion = int(input())

# if opcion == 1:
#     gradoscel = int (input("Introduzca la temperatura: "))
#     formula = 9 / 5 * gradoscel + 32
#     print (f"{formula} grados Fahrenheit")
# elif opcion == 2:
#     dolares = float(input ("Introduzca la cantidad de dolares: "))
#     tasa = 56.58
#     formula = dolares * tasa
#     print (f"{formula} pesos")
# elif opcion == 3:
#     metros = float (input("Introduzca la cantidad de metros: "))
#     formula = metros * 3.28084
#     print (f"{formula} pies")

# else:
#     print ("Gracias por usar nuestro programa ")


# 3- Hacer un programa que genere las tablas de multiplicar de los números
# múltiplos de 5 que hay entre 1 y 1000

# num = 1

# while num <=1000:
#     print (f"{num} x { 5 } = {num * 5}") # 1x5=5  <---Plantilla
#     num = num + 1

# 4- Realizar un programa que reciba por teclado el sueldo de un empleado y le
# aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)


renta1 = 416200     #excento
renta2 = 624329     #15%
renta3 = 867123     #20% , si excede de este tope 25%

sueldo = float(input ("Ingrese su sueldo: "))

if sueldo <= renta1:
    print("Su sueldo esta excento de cobro de ISR")

elif sueldo <= renta2:
    calc1 = sueldo - 416220
    calc2 = calc1 * 0.15
    calc3 = calc2 // 12
    afp = sueldo * 0.0287 // 12
    ars = sueldo * 0.0304 // 12

    print (f" Su retencion mensual des: IRS {calc3} pesos, AFP: {afp} pesos, ARS: {ars} pesos")

elif sueldo <= renta3:
    calc1 = sueldo - 624329
    calc2 = calc1 * 0.20
    calc3 = calc2 + 31216
    calc4 = calc3 // 12
    afp = sueldo * 0.0287 // 12
    ars = sueldo * 0.0304 // 12

    print (f" Su retencion mensual des: IRS {calc4} pesos, AFP: {afp} pesos, ARS: {ars} pesos")

elif sueldo >= renta3:
    calc1 = sueldo - 867123
    calc2 = calc1 * 0.25
    calc3 = calc2 + 79776
    calc4 = calc3 // 12
    afp = sueldo * 0.0287 // 12
    ars = sueldo * 0.0304 // 12

    print (f" Su retencion mensual des: IRS {calc4} pesos, AFP: {afp} pesos, ARS: {ars} pesos")

else:
    print ("Gracias por usar nuestro programa")




# 5-Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un
# límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100
# El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de
# retiro son 10,000 y 2000 pesos por transacción en caso contrario.
# El cajero debe informar si el monto solicitado no puede ser dispensado o si
# excede el límite de transacción. Y debe hacer la distribución de los billetes de
# acuerdo al monto. Por ejemplo, si el usuario solicita 3,900 y hay disponibilidad en
# todos los billetes, el cajero debe dispensar 3 billetes de mil, 1 de quinientos y 4 de
# cien.


