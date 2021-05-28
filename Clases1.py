#Clases

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False
    
    def arrancar (self):
        self.arrancado = True
        print ("El", self.marca, self.modelo, "ha arrancado")

    def parar (self):
        self.arrancado = False
        print ("El", self.marca, self.modelo, "se ha parado")


laguna = Coche ("Renault", "Laguna")
tesla = Coche ("Tesla", "Model 3")
corolla = Coche ("Toyota", "Hilux")

print (type (laguna))
print (type (tesla))
print (type (corolla))

print (laguna.marca, laguna.modelo)
print (tesla.marca, tesla.modelo)
print (corolla.marca, corolla.modelo)

laguna.arrancar()
tesla.arrancar()
corolla.arrancar()

print (laguna.arrancado)
print (tesla.arrancado)
print (corolla.arrancado)

laguna.parar()
tesla.parar()
corolla.parar()

print (laguna.arrancado)
print (tesla.arrancado)
print (corolla.arrancado)

