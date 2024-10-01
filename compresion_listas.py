# ¿Qué es la comprensión de listas?
# 
# En Python, la comprensión de listas es una característica que te permite crear listas 
# de una manera muy concisa y legible, en una sola línea de código. 
# En lugar de escribir un bucle for y agregar elementos a una lista uno por uno, 
# puedes utilizar la sintaxis de comprensión de listas para generar la lista completa de forma más directa.
# 
# ¿Cómo funciona?
# 
# La sintaxis básica de una comprensión de listas es la siguiente:
# nueva_lista = [expresión for elemento in iterable if condición]
# 
# expresión: El valor que se añadirá a la nueva lista para cada elemento.
# elemento: La variable que representa cada elemento del iterable.
# iterable: Cualquier objeto iterable como una lista, tupla, cadena, etc.
# condición: Una condición opcional que se evalúa para cada elemento. 
#            Si la condición es verdadera, el elemento se incluye en la nueva lista.

numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = [num for num in numeros if num % 2 == 0]
print(numeros_pares)

cuadrados = [x**2 for x in range(10)]
print(cuadrados)

palabras = ["manzana", "banana", "cereza"]
primeras_letras = [palabra[0] for palabra in palabras]
print(primeras_letras)

numeros = [1, 2, 3, 4, 5]
numeros_mayores_que_2 = [num for num in numeros if num > 2]
print(numeros_mayores_que_2)

