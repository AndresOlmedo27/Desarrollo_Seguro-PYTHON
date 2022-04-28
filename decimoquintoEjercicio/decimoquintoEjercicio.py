def front():
    
    print("Gesión del listín telefónico")
    print("============================")
    print("1 - Consultar un teléfono")
    print("2 - Añadir usuario y teléfono")
    print("3 - Eliminar un teléfono")
    print("4 - Crear listín")
    print("0 - Salir")
    print("============================")
    opciones = input("Introduce (número) la opción que quieres : ")
    return opciones

def darTelef(archivo, nombre):
    
    try: 
        arch = open(archivo, 'r')
    except FileNotFoundError:
        print("El fichero " + archivo +  " no existe\n")
    else:
        listTel = arch.readlines()
        arch.close()
        listTel = dict([tuple(line.split(',')) for line in listTel])
        if nombre in listTel:
            print (listTel[nombre])
        else:
            print("El cliente " + nombre + " no existe\n")


def añadirTelef(archivo, nombre, telefono):
    
    try: 
        arch = open(archivo, 'a')
    except FileNotFoundError:
        print("El fichero " + archivo + " no existe\n")
    else:
        arch.write(nombre + ',' + telefono + '\n')
        arch.close()
        print("El usuario y teléfono se han añadido.\n")

def eliminarTelef(archivo, nombre):
    
    try: 
        arch = open(archivo, 'r')
    except FileNotFoundError:
        print("El fichero " + archivo + " no existe\n")
    else:
        listTel = arch.readlines()
        arch.close()
        listTel = dict([tuple(prueba.split(",")) for prueba in listTel]) #La clase dict es un tipo mapa que asocia claves:valores.
        if nombre in listTel:
            del listTel[nombre]
            f = open(archivo, 'w')
            for nombre, telefono in listTel.items(): #.items Devuelve una vista de los pares clave: valor del diccionario.
                arch.write(nombre + "," + telefono)
            arch.close()
            print ("El cliente se ha borrado\n")
        else:
            print("El cliente " + nombre + " no existe\n")


def crearListTel(archivo):
   
    import os
    if os.path.isfile(archivo): # Este método devuelve true si hay un archivo igual al pasado por parámetro
        entrada = input("El fichero " + archivo + " ya existe. ¿Desea borrar su contendio? (Si/No)? ")
        if entrada == "No": 
            print ("El fichero no se ha borrado.\n")
    arch = open(archivo, 'w')
    arch.close()
    print ("Se ha creado el fichero.\n")

     
def listin():
    
    archivo = 'listin.txt' 
    while True:
        opciones = front()
        if opciones == "1":
            nombre = input("Introduce el nombre del usuario: ")
            print(darTelef(archivo, nombre))
        elif opciones == "2":
            nombre = input("Introduce el nombre del usuario: ")
            telefono = input("Introduce el teléfono del usuario: ")
            print(añadirTelef(archivo, nombre, telefono))
        elif opciones == "3":
            nombre = input("Introduce el nombre del usuario: ")
            print(eliminarTelef(archivo, nombre))
        elif opciones == "4":
            print(crearListTel(archivo))
        elif opciones == "0":
            break
        else:
            print("Introduce un número de la lista")
    return 

listin()




