# Ejercicio 10
# Escribir un programa que almacene los números de 0 a 35 en una lista, elimine
# de la lista los números que ocupen posiciones múltiplos de 3, y muestre por
#  pantalla la lista resultante.



numeros = []
for i in range(0, 36):
    numeros.append(i)
    prueba = numeros[i] % 3
    if prueba !=0:
        print(numeros[i])
 