# Ejercicio 11
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%



from multiprocessing.sharedctypes import Value
from tkinter import N



num = 0
porIVA = 0
validar = False 
       
while not validar:
        try:
            num  = input("Introduce un número: \n ")
            num = float(num)
    
            if num < 0:
                print("El número debe ser mayor que 0.")
                break
            elif num == 0:
                print("El número debe ser mayor que 0.")
                break
            
            porIVA = input("Introduce el porcentaje de IVA a calcular: \n")
            porIVA = int(porIVA)
            if porIVA == 0:
                print("No has introducido ningún porcentaje para el valor %d" % (num)
                            + ". Se le asigna automáticamente un 21%.")
                num = num / 100*21
                print(num)
            elif porIVA < 0:
                print("El porcentaje debe ser mayor que 0.")
                break
            else:
                print("El valor que has introducido es '%d' " % (num)+", al que"
                + " se le va a aplicar un porcentaje del %d" % (porIVA) + "%." )

                op = num / 100
                ivaTotal = porIVA * op
                precioTotal = ivaTotal + num
                print("El resultado de aplicarle a '%d'" % (num)+ " este porcentaje son %d" % (ivaTotal)
                +" euros, así que el precio total de la factura es de %d " % (precioTotal) + "euros.")
                validar = True

        except ValueError:
            print("Error.")
            break

        
            
            

