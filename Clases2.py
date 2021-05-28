class Cliente:
    def __init__(self, nombre, apellido, telefono ):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = None

    def mostrar_cliente(self):
        print ("Nombre:{} Apellido:{} Telefono:{}".format(self.nombre, self.apellido, self.telefono))


c1 = Cliente("John", "Snow","809-220-1111")
c2 = Cliente("Anna", "Snow","809-220-1113")
c3 = Cliente("Tonny", "Stark","809-777-8888")

c1.mostrar_cliente()
c2.mostrar_cliente()
c3.mostrar_cliente()





