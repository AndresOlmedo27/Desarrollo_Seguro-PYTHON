
# Ejercicio 2
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo 
# es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número
#  de teléfono sin el prefijo y la extensión. Además, debe reconocer el prefijo la comunidad autónoma.



from imp import NullImporter
from pickletools import OpcodeInfo
import re


prefijo= "+34"
validar= False

numeroTel = input("Introduce tu número de teléfono: ")

while(not validar):

    try:

        if(re.search("[^\\d]", numeroTel)):
            print("Introduce solo números :)")
            nombre= input("Introduce tu número de teléfono: ")
        else:
            print("Gracias.")
            validar = True
    except Exception:
        print("Ha ocurrido un error.")
        break

numeroTel2= numeroTel

extension = input("Introduce la extensión: ")

while(validar):

    try:

        if(re.search("[^\\d]", extension)):
            print("Introduce solo números :)")
            nombre= input("Introduce la extensión: ")
        else:
            print("Gracias.")
            validar = False
    except Exception:
        print("Ha ocurrido un error.")
        break

extension2= extension

input("Este es tu número completo: " + prefijo+ "-"+ numeroTel2+ "-"+ extension2)

pref = numeroTel2[0:3]
input(pref)

if pref > 910 and pref < 919:
    print("El prefijo " + pref + " pertenece a Madrid")
