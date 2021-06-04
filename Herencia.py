# class Base:
#     def metodo_base(self):
#         print ("Se ha ejecutado el metido base")
    
#     def imprimir(self, valor):
#         print(valor)

# class Hija (Base):
#     pass

# h1 = Hija()

# h1.imprimir
# h1.metodo_base

class Persona:
    def __init__(self, nombre, apellido, telefono ):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = None


class Cliente(Persona):
    def __init__(self, nombre, apellido, telefono):
        Persona().__init__(nombre,apellido,telefono)
        print ("Se a creado un nuevo cliente")

    def mostrar_cliente(self):
        print ("Nombre:{} Apellido:{} Telefono:{}".format(self.nombre, self.apellido, self.telefono))

c1 = Cliente()
c1.apellido


class Empleado(Persona):
    def __init__(self, nombre, apellido, telefono, salario):
        Persona().__init__(nombre,apellido,telefono)
        self.salario = salario

    def aumentar_sueldo(self, aumento):
        self.salario += aumento

em1 = Empleado()
em1.nombre