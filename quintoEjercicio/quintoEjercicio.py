
# Ejercicio 5
# Escribir un programa que pida al usuario dos números enteros y
# muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m>
# son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

from codecs import CodecInfo


num1 = input("Introduce un número entero: ")
num1 = int(num1)
num2 = input("Introduce un número entero: ")
num2 = int(num2)
try:

        if num1 > 0 and num2 > 0:
            cociente = num1 / num2
            print("El cociente resultante de dividir %d" % (num1) + " entre %d" % (num2) + " es %d" % (cociente))
            resto = num1 % num2
            print("El resto resultante de dividir %d" % (num1) + " entre %d" % (num2) + " es %d" % (resto))
        else:
            print("Los números deben ser mayor que 0.")

except ValueError:
    print("Error. Solo números enteros.")
    
