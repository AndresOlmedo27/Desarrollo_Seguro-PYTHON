
# Ejercicio 7
# En una determinada empresa, sus productos son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores opiniones. Los puntos que pueden conseguir los productos pueden ser 0.0, 0.4, 0.6 o más, 
# pero no valores intermedios entre las cifras mencionadas. A continuación, se muestra una tabla con los niveles
# correspondientes a cada puntuación. La cantidad de reputación conseguida en cada nivel es de 1.5 puntos multiplicada 
# por la puntuación del nivel.
# Mal producto: 0.0 (1.5 x 0.0)
# Aceptable: 0.4	(1.5x0.4)
# Reseñable: 0.6 o más (1.5x0.6)
# Escribir un programa que lea la puntuación del producto e indique su nivel 
# de evaluación, así como la reputación del producto.

# validar = False

malProducto = 0
aceptable = 0.4
reseñable = 0.6
puntos = float(input("Introduce tu puntuación: "))

try:
    if puntos == malProducto:
        print("Mal producto. Puntuación y reputación de 0.0 puntos. ")
    elif puntos == aceptable:
        print("Aceptable. Puntuación de 0.4 puntos y reputación de 0.6 puntos.")
    elif puntos == reseñable:    
        print("Reseñable. Puntuación de 0.6 puntos y reputación de 0.9 puntos")    
    else:
        print("Elige una puntuación entre las siguiente: 0.0 , 0.4 , 0.6")
        
except ValueError:
    print("hols")