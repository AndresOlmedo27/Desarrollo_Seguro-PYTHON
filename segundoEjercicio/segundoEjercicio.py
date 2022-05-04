
# Ejercicio 2
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo
# es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
# Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número
#  de teléfono sin el prefijo y la extensión. Además, debe reconocer el prefijo la comunidad autónoma.


from imp import NullImporter
from pickletools import OpcodeInfo
import re


prefijo = 34
validar = False

numeroTel = input("Introduce tu número de teléfono: ")

while(not validar):

    try:

        if(re.search("[^\\d]", numeroTel)):
            print("Introduce solo números :)")
            numeroTel = input("Introduce tu número de teléfono: ")
        else:
            print("Gracias.")
            validar = True
    except Exception:
        print("Ha ocurrido un error.")
        break


numeroTel2 = numeroTel

extension = input("Introduce la extensión: ")

while(validar):

    try:

        if(re.search("[^\\d]", extension)):
            print("Introduce solo números :)")
            extension = input("Introduce la extensión: ")
        else:
            print("Gracias.")
            validar = False
    except Exception:
        print("Ha ocurrido un error.")
        break

# extension2= extension

print("Este es tu número: " + numeroTel)


pref = int(numeroTel2[0:3])  # cambiar variable de string a entero
# print(pref)

if pref >= 911 and pref <= 918:
        prefij = str(pref)  # cambiar variable de entero a string
        print("El prefijo " + prefij + " pertenece a la C. de Madrid")
elif pref == 856 or pref == 858:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Andalucía")
elif pref >= 950 and pref <= 959:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Andalucía")

elif pref == 974 or pref == 976:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Aragón")

elif pref == 978 or pref == 876:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Aragón")
elif pref >= 984 and pref <= 985:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece al Principado de Asturias")
elif pref == 871:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de las Islas Baleares")
elif pref == 822 or pref == 828:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de las Islas Canarias")
elif pref == 922 or pref == 928:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de las Islas Canarias")
elif pref == 942:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Cantabria")
elif pref == 925 or pref == 926:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Toledo")
elif pref == 949 or pref == 967:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Toledo")
elif pref == 969:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Toledo")
elif pref == 925 or pref == 926:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Toledo")
elif pref == 921 or pref == 923:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Andalucía")
elif pref == 947 or pref == 975:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Andalucía")
elif pref == 979 or pref == 980:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Andalucía")
elif pref == 983 or pref == 987:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Andalucía")
elif pref == 872 or pref == 873:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Cataluña")
elif pref == 877 or pref == 977:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Cataluña")
elif pref >= 931 and pref <= 937:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Cataluña")
elif pref == 972 or pref == 973:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Cataluña")
elif pref == 824 or pref == 927:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Extremadura")
elif pref == 924:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Extremadura")
elif pref == 881 or pref == 986:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Galicia")
elif pref == 981 or pref == 982:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Galicia")
elif pref == 986 or pref == 988:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Galicia")
elif pref == 941:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de La Rioja")
elif pref == 968:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. de Murcia")
elif pref == 848 or pref == 948:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. Foral de Navarra")
elif pref == 943 or pref == 945:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. del País Vasco")
elif pref == 960 or pref == 966:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. Valenciana")
elif pref == 965:
        prefij = str(pref)
        print("El prefijo "+prefij + " pertenece a la C. Valenciana")
else:
        print("El número introducido no corresponde con ninguno reconocido. Por favor, introduzca uno válido")
