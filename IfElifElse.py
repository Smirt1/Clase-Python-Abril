
#if elif else

tienes_llave = input ("Tienes una llave?: ") 

if tienes_llave == "si":
    forma = input ("Que forma tiene la llave?: ")
    color = input ("Que color tiene la llave?: ")
    if forma == "cuadrada" and color =="rojo":
        print ("Puedes pasar por la Puerta 1")
    elif forma == "redonda" and color =="amarillo":
        print ("Puedes pasar por la Puerta 2")
    elif forma == "triangular" and color == "rojo":
        print ("Puedes pasar por la Puerta 2")
    else:
        print ("Tienes la llave equivocada")

print ("Fin")
