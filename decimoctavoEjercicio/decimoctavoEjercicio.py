# Ejercicio 18
# Se leen 2 números en formato string, 
# hay que implementar la suma según nos la enseñaron en el colegio, es decir:
# Desde el dígito menos significativo al más significativo (de derecha a izquierda):

# Se suman los dígitos de los dos números de la misma posición, 
# si la cifra resultante es >=10, se añade un 1 a la suma de los dígitos de la posición anterior.
# La cifra resultante (módulo 10) es el resultado de esa posición.

try:
    num1 = input("Introduce un número para sumar: \n")
    num1 = int(num1)
    num2 = input("Introduce otro número: \n")
    num2 = int(num2)

    lista1 = [num1]
    lista2 = [num2]
    lista3 = [x + y for x, y in zip(lista1, lista2)]
    print(lista3)
except ValueError:
    print("Sólo números.")