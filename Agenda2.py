
telefonos = {"Smirt": 8096394000,"Max":8092228888,"Payne":8097779898, "Rose":8093338888 }

consultando = True

while consultando:
    print()
    print("Mi Agenda telefonica")
    print("------------")
    print("1. Consultar")
    print("2. Anadir")
    print("3. Modificar")
    print("4. Borrar")
    print("5. Salir")
    print("------------")

    opcion = ""
    while opcion not in ("1", "2", "3", "4","5"):
        opcion = input("-->")

    if opcion == "1":
        nombre = input("Nombre: ")
        if nombre not in telefonos:
            print ("Ese nombre no existe.")
        else:
            telf = telefonos[nombre]
            print (nombre, ":", telf)

    elif opcion == "2":
        nombre = input ("Nombre: ")
        if nombre in telefonos:
            print ("Ese nombre ya esta en la agenda")
        else:
            telf = int (input("Telefono: "))
            telefonos [nombre] = telf
            print ("El telefono se ha anadido correctamente")


    elif opcion == "3":
        nombre = input ("Nombre: ")
        if nombre not in telefonos:
            print ("Ese nombre no esta en la agenda")
        else:
            telf = int(input ("Telefono: "))
            telefonos [nombre] = telf
            print ("El telefono se ha modificado correctamente")

    elif opcion == "4": 
        nombre = input ("Nombre: ")
        if nombre not in telefonos:
             print ("Ese nombre no esa en la agenda")
        else:
            del telefonos[nombre]
            print ("El telefono se ha borrado correctamente")

    elif opcion == "5":
        consultando = False



        
