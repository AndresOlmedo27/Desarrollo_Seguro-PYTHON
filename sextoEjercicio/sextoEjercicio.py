
# Ejercicio 6

# Una farmacia tiene mucho éxito en dos de sus productos: mascarillas y gel hidroalcohólico.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
# calcular el peso de las mascarillas y geles que saldrán en cada paquete a demanda. Cada mascarilla pesa 112 g y
# cada gel 250 g. Escribir un programa que lea el número de mascarillas y geles vendidos en el último pedido y calcule
# el peso total del paquete que será enviado.

import re


regEx = "[^(\\d)]+"
validar = False
pesoMasc = 112
pesoGel = 250

mascarillas = input("Introduce el número de mascarillas que quieres pedir: \n")

match = re.search(regEx, mascarillas)

while not validar:

    try:
        if (not match):
            # input("Gracias")
            validar = True
            
        else:
            print("Introduce una cantidad númerica positiva.")
            break
            # mascarillas = input("Introduce el número de mascarillas que quieres pedir: \n")
            
    except ValueError:
        print("Solo valores numéricos.")

while validar:

    try:
        if (not match):
            geles = input("Introduce el número de geles que quieres pedir: \n")
            validar = False
            
        else:
            print("Introduce una cantidad númerica positiva.")
            geles = input("Introduce el número de mascarillas que quieres pedir: \n")
            

    except ValueError:
        print("Solo valores numéricos.") 


mascarillas = int(mascarillas)

if mascarillas == 0:
    print("No has saleccionado ninguna mascarilla.")
elif mascarillas == 1:
    print("Has seleccionado una mascarilla")
else:
    print("Has seleccionado %d " % (mascarillas) + "mascarillas.")

       
geles = int(geles)

if geles < 0:
    print("Introduce un valor posivito.")

elif geles == 0:
    print("No has saleccionado ningun gel.")
elif mascarillas == 1:
    print("Has seleccionado un gel")
else:
    print("Has seleccionado %d " % (geles) + "geles.")

mascTotal = mascarillas * pesoMasc
gelTotal = geles * pesoGel
envio = mascTotal + gelTotal

print("El peso total del envío es: %d" % (envio) + "gramos")
    
