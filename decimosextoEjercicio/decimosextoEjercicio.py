
cantidad = 5
lista = []
print (f"Introduce {cantidad} números")
try:
    for i in range(cantidad):
        numeros = input(f"Introduce el número {i + 1}: ")
        numero = int(numeros)
        lista.append(numero)
    print("Estos son tus números: ")
    for x in lista:
        print(x)

    enesimo  = input("Introduce el número a evaluar: \n")
    enesimo = int(enesimo)
    if not enesimo > cantidad:
        long = len(lista)
        lista.sort()
        print(f"El {enesimo}º mayor número es: ")
        print(lista[long-enesimo])

    else:
        print("El número a evaluar debe ser menor que el tamaño total.")
except Exception:
    print("Error.")
