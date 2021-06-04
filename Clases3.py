class Humano:
    def __init__(self):
        self.edad = 25
        print ("Soy un objeto nuevo")

    def hablar(self, mensaje):
        print (mensaje)

pedro = Humano()
raul = Humano ()

print ("Soy Pedro y tengo", pedro.edad )
print ("Soy Raul y tengo", raul.edad )

pedro.hablar ("Hola")
raul.hablar ("Hola, Pedro!")