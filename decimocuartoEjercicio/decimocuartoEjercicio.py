import re

f = "C:\\Users\\afolmedo\\OneDrive - Indra\\Escritorio\\EjerciciosJAVA\\decimoctavoEjercicio\\decimoctavoEjercicio.java"
regEx = "\\.[^txt]+"
try:
    op = open(f, "r") 
    if(not re.search(regEx, f)):
        
        for linea in op:
            print(linea)
            print("El número de palabras que contiene el archivo son: ")
            print(len(linea.split()))
            
    else:
        print("Introduce un formato válido.")
    op.close()   
except FileNotFoundError:
    print("Archivo no encontrado")
