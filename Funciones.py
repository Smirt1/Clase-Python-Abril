# suma = 7 + 8 + 9
# media = suma / 3

# print ("La puntuacion de la clase es: ", media)

# def puntuacion (alum1, alum2, alum3):
#     suma = alum1 + alum2 + alum3
#     return suma / 3

# media = puntuacion(7,8,9)
# print ("La puntuacion de esta clase es: ", media)

# media = puntuacion(10,15,9)
# print ("La puntuacion de esta clase es: ", media)

def puntuacion (clase):
    return sum (clase) / len (clase)

clase = [7, 8, 9]
media = puntuacion (clase)
print ("La puntuacion de esta clase es: ", media)

clase = [5, 6, 7.5, 10]
media = puntuacion(clase)
print ("La puntuacion de esta clase es: ", media)