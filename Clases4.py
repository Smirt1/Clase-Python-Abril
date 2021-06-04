class Gato:
    pass

mi_gato = Gato()


class Aritmetica:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumar (self):
        suma = self.valor1 + self.valor2
        print ("El resultado de la suma es: ", suma)

    def restar (self):
        resta = self.valor1 - self.valor2
        print ("El resultado de la resta es: ", resta)

    
    def multip (self):
        multiplicar = self.valor1 * self.valor2
        print ("El resultado de la multiplicacion es: ", multiplicar)
    

sum1 = Aritmetica(2,2)
sum1.sumar()

rest1 = Aritmetica (5,3)
rest1.restar()

mult1 = Aritmetica(5,2)
mult1.multip()