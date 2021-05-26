#FIRST PROGRAM

# print ("200 is a great number")

#STRINGS AND NUMBERS OPERATIONS AND CONCATENATION

# print (20 * 24 * 60)
#print ("20 days are " + str(50) + " minutes") #concatenacion

#print (f"20 days are {50} minutes")

#VARIABLES

# calcu_to_minutes = 24 * 60
# name_of_unit = "minutes"

# print(f"20 days are {20 * calcu_to_minutes} {name_of_unit}")
# print(f"35 days are {35 * calcu_to_minutes} {name_of_unit}")

#FUNCIONES

# calcu_to_minutes = 24
# name_of_unit = "minutes"

# def days_to_units():
#     print(f"20 days are {20 * calcu_to_minutes} {name_of_unit}")
#     print("All good!")

# days_to_units()


# calcu_to_minutes = 24
# name_of_unit = "minutes"

# def days_to_units(days, mensaje):
#     print(f"{days} days are {days * calcu_to_minutes} {name_of_unit}")
#     print(mensaje)

# days_to_units(20, "Good!!!")
# days_to_units(12, "Dear lord!!")
# days_to_units(55,"Yo are killing python")
# days_to_units(888, "Sooooo good")

#INPUT FUNCIONES RETURN


# calcu_to_minutes = 24
# name_of_unit = "minutes"

# def days_to_units(days):
#     return(f"{days} days are {days * calcu_to_minutes} {name_of_unit}")


# user_input = int (input("Hey user, enter a numbert of days an I will convert it to minutes!\n"))
# calcu_value = days_to_units(user_input)
# print (calcu_value)

# def multiplicar (a,b):
#     print (a*b)

# multiplicar(10,5)


# def multiplicar (a,b):
#     return (a*b)

# resultado = multiplicar(10,5) +  5
# print (resultado)

# def promedio (alum1, alum2, alum3):
#     suma = alum1 + alum2 + alum3
#     return suma / 3

# media = promedio(7,8,9)
# print ("El promedio de la clase es: ", media)

# media = promedio(5,6,7.5)
# print ("El promedio de la clase es: ", media)

# #walk

numero = 10
otro = 3

suma = numero + otro
dif = numero - otro
mult = numero * otro
div = numero / otro
resto = numero % otro

print (suma)
print (dif)
print (mult)
print (div)
print (resto)


