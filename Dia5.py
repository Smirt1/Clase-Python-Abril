
#class

class Carro:
    cantidad_combustible = 10
    cantidad_puertas = 4
    def encender(self):
        pass
    def apagar(self):
        pass


corolla = Carro()
corolla.encender()
corolla.apagar()

civic = Carro()
civic.encender()
civic.apagar()

print(corolla.cantidad_puertas)
print(civic.cantidad_puertas)


#class

class Persona:
    nombre = ''
    apellido = ''
    telefono = ''

def mostrar_nombre(self):
    print(f"self.nombre,self.apellido")

class Empleado(Persona):
    salario = 0

class Cliente(Persona):
    pass

class Proveedor(Persona):
    compania = ''

empleado1 = Empleado()
empleado1.apellido()

print(empleado1.apellido)







