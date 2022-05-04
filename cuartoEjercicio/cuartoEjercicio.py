# Ejercicio 4
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y
# después muestre en pantalla la suma de todos los enteros desde 1 hasta n.

regEx = ""
fin = 0

num1 = input("Introduce un número entero: ")
num1 = int(num1)
try:
    if num1 > 0:
       
            for num11 in range(num1):
                print("%d" % (fin) + " + " + "%d" % num11)
                fin = fin + num11
                print("El resultado es %d" % (fin))
    else:
        print("Introduce un número entero.")
except Exception:
    print("Introduce sólo números.")