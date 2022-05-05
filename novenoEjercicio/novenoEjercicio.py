# Ejercicio 9
# Escribir un programa que muestre el eco de todo lo que el usuario
# introduzca hasta que el usuario escriba “BASTA!” que terminará.

import re
validar = False
regEx = "[^(a-zA-Z)^(\!)]+"
stop = "BASTA!"

rep = input("Introduce una palabra: \n")

while not validar:
    try:
        if (re.search(regEx, rep)):

            print("Formato no admitido.")
            rep = input("Introduce una palabra: \n")

        elif rep == "BASTA!":
                # validar = True
                break

        else:
            
            print(rep)
            rep = input("Introduce una palabra: \n")
            
    except Exception:
        print("Error.")