#Modele tres entidades del mundo real, colocar por lo menos 3 características distintivas.

# class Carro:
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
       

# class Computadora:
#     def __init__(self, procesador, memoria, monitor):
#         self.procesador = procesador
#         self.memoria = memoria
#         self.monitor = monitor

# class Libro:
#     def __init__(self, autor, dedicatoria, indice):
#         self.autor = autor
#         self.dedicatoria = dedicatoria
#         self.dedicatoria = indice


#Crear una clase llamada Estudiante con un campo llamado promedio, el cual solo podrá ser accedido mediante un metodo.
# El valor del promedio no puede estar por encima de 100 que es la nota máxima.

# class Estudiante:
#     def __init__(self, nombre, curso, promedio):
#         self.nombre = nombre
#         self.curso = curso
#         self.promedio = promedio

#     def mostrar_promedio(self):
#         print (" Nombre: {}, Curso: {}, Promedio: {}".format (self.nombre, self.curso, self.promedio))


# est1 = Estudiante ("Pedro", "8vo", "80")
# est2 = Estudiante ("Maria","5to", "90")
# est1.mostrar_promedio()
# est2.mostrar_promedio()

#Hacer una clase llamada Aritmética, que contenga métodos para cada una de las operaciones aritméticas básicas.

# class Aritmetica:
#     def __init__(self, valor1, valor2):
#         self.valor1 = valor1
#         self.valor2 = valor2

#     def sumar (self):
#         suma = self.valor1 + self.valor2
#         print ("El resultado de la suma es: ", suma)

#     def restar (self):
#         resta = self.valor1 - self.valor2
#         print ("El resultado de la resta es: ", resta)

    
#     def multip (self):
#         multiplicar = self.valor1 * self.valor2
#         print ("El resultado de la multiplicacion es: ", multiplicar)
    

# sum1 = Aritmetica(2,2)
# sum1.sumar()

# rest1 = Aritmetica (5,3)
# rest1.restar()

# mult1 = Aritmetica(5,2)
# mult1.multip()


# Cree una clase llamada Personaje con los métodos de instancia MoverArriba, MoverAbajo, MoverDerecha y MoverIzquierda. Cree una clase llamada Mario y
# otra clase llamada Koopa que herede las funcionalidades de la clase Personaje.

# class Personaje:
#     def __init__(self, nombre, ocupacion):
#         self.nombre = nombre
#         self.ocupacion = ocupacion
#         self.MoverArriba = True
#         self.MoverAbajo = True
#         self.MoverDerecha = True
#         self.MoverIzquierda = True

#     def moverarriba (self):
#         self.MoverArriba = True
#         print ("El personaje", self.nombre, "se ha movido hacia arriba")

#     def moverabajo (self):
#         self.MoverAbajo = True
#         print ("El personaje", self.nombre, "se ha movido hacia abajo")

#     def moverderecha (self):
#         self.MoverDerecha = True
#         print ("El personaje", self.nombre, "se ha movido hacia la derecha")

#     def moverizquierda (self):
#         self.MoverIzquierda = True
#         print ("El personaje", self.nombre, "se ha movido hacia la izquierda")


# class Mario (Personaje):
#     def __init__(self, nombre, ocupacion):
#         Personaje().__init__(nombre, ocupacion)   


# class Koopa (Personaje):
#     def __init__(self, nombre, ocupacion):
#         Personaje().__init__(nombre, ocupacion)
       
        
# pers1 = Personaje ("Mario",  "plomero")
# pers2 = Personaje ("Koopa", "villano")

# print (pers1.nombre, pers1.ocupacion)
# print (pers2.nombre, pers2.ocupacion)

# pers1.moverarriba()
# pers2.moverabajo()

# print (pers1)
# print (pers2)


# Cree una clase Carro, con un campo llamado _cantidadCombustible y un método que se llame Encender el cual en base a la gasolina disponible 
# mostrara si el carro pudo o no avanzar. Cada vez que el método se ejecute, deberá restarse 1 a la gasolina disponible. La cantidad de gasolina debe
# establecerse al momento de instanciar un objeto de del tipo de la clase.

class Carro():
    def __init__(self, cantidad):
        self.cantidad_conmbustible = cantidad

    def encender(self):
        if self.cantidad_combustible > 0:
            print ("El auto encendio")
            self.cantidad_combustible -= 1
        else:
            print ("No tiene combustible")

