
# Ejercicio 3
# Escribir un programa que pregunte por consola por los animales de un zoo, separados por asteriscos,
# y muestre por pantalla cada uno de los animales en una línea distinta.


import re

regEx = "[^(a-zA-Z)(\\s)(\*)]+"
validar = False
zoo = input("Introduce los animales del zoo: ")
while(not validar):

    try:
        match = re.search(regEx, zoo)

        if(not match):
            n = [zoo]
            for zoo2 in n:
                zoo3 = zoo2.replace("*", "\n")
                print(zoo3)
                validar = True
        else:
            print("Introduce solo caracteres :)")
            zoo = input("Introduce los animales del zoo: ")

    except Exception:
        print("Ha ocurrido un error")
        break
