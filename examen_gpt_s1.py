# Sección 1: Fundamentos de Python
# Variables y Tipos de Datos:
# ¿Qué diferencia hay entre una lista, una tupla y un diccionario en Python? Da un ejemplo de cada uno.
# Lista: es un conjunto de datos ordenados de uno o varios tipos de datos, se ordenan por indice y son mutables, se representan con llaves cuadradas
lista = [1,'abc', True, 7, 80.2]
print(lista)
# tuplas: son un conjunto de datos ordenado de uno o varios tipos de datos, se ordenan por indice pero son inmutables, se representan con parentesis
tupla = (1,'abc', True, 7, 80.2)
print(tupla)
# diccionario: es un conjunto de datos representado con una clave y valor lo que permite ordenarlos internamente en tablas hash, es mutable y se representa con corchetes
diccionario = {'texto': 'Hola', 'numero': 123, 'Bool': True}

# Control de Flujo:
# Escribe un bucle for que imprima los números del 1 al 10.
for numero in range(1,11):
    print(numero)
# ¿Cuál es la diferencia entre break y continue en un bucle?
# contiue permite seguir iterando el bucle
# break interrumpe la iteracion y cierra el bucle


# Funciones:
# Escribe una función que acepte dos números como parámetros y devuelva su suma.
def suma(numero1, numero2):
    return numero1 + numero2

print(suma(23,55))
# ¿Qué es un argumento por defecto en una función? Da un ejemplo.
# un argumento por defecto es una variable que tiene un valor fijo siempre y cuando este no sea pasado como argumento en el llamado de la funcion
# ejemplo
def multiplica(numero1, numero2 = 1):
    return numero1 * numero2

# llamado con todos los argumentos
print(multiplica(9, 9))
# llamado con argumento por defecto
print(multiplica(9))

# Comprensión de Listas:
# Usa una list comprehension para crear una lista de los cuadrados de los números del 1 al 5.
lista_comprension = [x ** 2 for x in range(1,6)]
print(lista_comprension)

