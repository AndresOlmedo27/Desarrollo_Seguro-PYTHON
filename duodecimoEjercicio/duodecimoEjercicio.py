# Ejercicio 12



# Escribir un programa que reciba una cadena de caracteres y 
# devuelva un diccionario con cada palabra que contiene y su frecuencia.
frase = input("Introduce una frase: \n")
print("Tu frase es --> " + frase)


try:
        lista1 = frase.split()
        dicc = {}
        for i in lista1:
            if i in dicc:
                dicc[i] += 1
            else:
                dicc[i] = 1
        print(dicc)

except Exception:
        print("Error.")
        
# Escribir otra función que reciba el diccionario generado con la función anterior y 
# devuelva una tupla con la palabra más repetida y su frecuencia.