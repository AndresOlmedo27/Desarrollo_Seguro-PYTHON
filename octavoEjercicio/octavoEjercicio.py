# Ejercicio 8
# Escribir un programa en el que se pregunte al usuario por una frase y 
# una letra, y muestre por pantalla el número de veces que aparece la letra en la frase y 
# el número total de caracteres de la frase sin espacios en blanco.

frase = input("Introduce una frase: \n")
letra = input("Introduce una letra: \n")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %d veces en la frase '%s'." % (letra, contador, frase))

frase2 = frase.replace(" ", "")
# print(frase2)
longitud = len(frase2)
print("El número total de caractéres de la frase "+"\""+ frase2+"\""+" es de %d" % (longitud))

# faltan medidas de seguridad