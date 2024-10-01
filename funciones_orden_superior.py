
# Funciones de orden superior
# Una función de orden superior en Python 
# es una función que puede aceptar otras funciones como argumentos y/o devolver una función como resultado. 
# Este concepto es fundamental en la programación funcional y permite escribir código más flexible y modular.

from functools import reduce

def aplicar_operacion(x, y, operacion):
    return operacion(x, y)

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

# Usando la función de orden superior
resultado_suma = aplicar_operacion(5, 3, sumar)
resultado_multiplicacion = aplicar_operacion(5, 3, multiplicar)

print(resultado_suma)  # Salida: 8
print(resultado_multiplicacion)  # Salida: 15

# En este ejemplo, `aplicar_operacion` es una función de orden superior 
# porque toma otra función (`operacion`) como argumento y la ejecuta con los parámetros `x` y `y`.

# Las funciones de orden superior son muy útiles cuando se combinan 
# con funciones como `map`, `filter` y `reduce`. 
# Aquí tienes un ejemplo usando `filter` para obtener solo los números pares de una lista:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6, 8, 10]

# Un closure en Python es una función anidada que recuerda 
# y accede a las variables de su función contenedora, 
# incluso después de que esta función contenedora haya finalizado su ejecución1. 
# Esto permite que la función interna “capture” el entorno en el que fue creada.

def exterior(x):
    def interior(y):
        return x + y
    return interior

closure = exterior(10)
print(closure(5))  # Salida: 15

# En este ejemplo: 
# La función exterior define una variable x y una función anidada interior.
# La función interior utiliza la variable x de la función contenedora.
# Cuando exterior se llama con el argumento 10, devuelve la función interior.
# La función devuelta (closure) recuerda el valor de x incluso después de que exterior haya terminado su ejecución.

# MAPS
# La función map() en Python se utiliza para aplicar una función a cada elemento de un iterable 
# (como una lista o una tupla) y devolver un nuevo iterable con los resultados. 
# Es especialmente útil para evitar bucles explícitos y hacer el código más conciso.

def cuadrado(n):
    return n * n

numeros = [1, 2, 3, 4, 5]
resultado = map(cuadrado, numeros)

# Convertimos el resultado a una lista para verlo
print(list(resultado))  # Salida: [1, 4, 9, 16, 25]

# Se puede simplificar aún más el código utilizando una función lambda:
numeros = [1, 2, 3, 4, 5]
resultado = map(lambda x: x * x, numeros)
print(list(resultado))  # Salida: [1, 4, 9, 16, 25]

# map() también puede aceptar múltiples iterables, 
# aplicando la función a los elementos correspondientes de cada iterable:
a = [1, 2, 3]
b = [4, 5, 6]
resultado = map(lambda x, y: x + y, a, b)
print(list(resultado))  # Salida: [5, 7, 9]

# FILTER
# La función filter() en Python se utiliza para crear un nuevo 
# iterable a partir de un iterable existente, filtrando los elementos 
# que no cumplen una condición específica. Es muy útil para trabajar con listas y otros iterables de manera eficiente.

def es_par(n):
    return n % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filter(es_par, numeros)

# Convertimos el resultado a una lista para verlo
print(list(resultado))  # Salida: [2, 4, 6, 8, 10]

# Puedes simplificar el código utilizando una función lambda:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filter(lambda x: x % 2 == 0, numeros)
print(list(resultado))  # Salida: [2, 4, 6, 8, 10]

# También puedes usar filter() para trabajar con objetos más complejos. 
# Por ejemplo, supongamos que tienes una lista de personas y quieres filtrar solo las que son menores de edad:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manuel", 78),
    Persona("Eduardo", 12)
]

menores = filter(lambda persona: persona.edad < 18, personas)
for menor in menores:
    print(f"{menor.nombre} de {menor.edad} años")
# Salida:
# Marta de 16 años
# Eduardo de 12 años

# REDUCE
# La función reduce() en Python se utiliza para aplicar una función de manera acumulativa 
# a los elementos de un iterable, reduciéndolo a un solo valor. 
# A diferencia de map() y filter(), reduce() no devuelve un nuevo iterable, sino un único valor.

numeros = [1,2,3,4,5]

def suma(a,b):
    return a + b

resultado = reduce(suma, numeros)
print(resultado)

# Simplificando el código utilizando una función lambda:
numeros = [1,2,3,4,5]

resultado = reduce(lambda a, b: a + b, numeros)
print(resultado)

# Con Valor Inicial 
# Puedo proporcionar un valor inicial que se utilizará 
# como el primer argumento en la primera llamada a la función:

numeros = [1, 2, 3, 4, 5]
resultado = reduce(lambda a, b: a + b, numeros, 10)
print(resultado)  # Salida: 25












