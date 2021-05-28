
#if elif else



tienes_llave = input ("Tienes una llave?: ") 


if tienes_llave == "si":
    forma = input ("Que forma tiene la llave?: ")
    color = input ("Que color tiene la llave?: ")
    
if tienes_llave != "si":
        print ("Si no tienes llaves no entras")
        
if forma == "cuadrada" and color =="roja":
     print ("Puedes pasar por la Puerta 1")
elif forma == "redonda" and color =="amarilla":
        print ("Puedes pasar por la Puerta 2")
elif forma == "triangular" and color == "roja":
        print ("Puedes pasar por la Puerta 2")
else:
    print ("Tienes la llave equivocada")
        
