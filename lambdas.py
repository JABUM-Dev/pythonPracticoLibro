# Lambdas o funciones anonimas 
# Una función lambda en Python es una función anónima, 
# lo que significa que no tiene un nombre definido. 
# Estas funciones son útiles para operaciones simples y rápidas. 
# La sintaxis básica de una función lambda es: lambda argumentos: expresión

# Sumando dos números 
sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(10, 2))

suma = lambda x, y: x + y
print(suma(3, 4))  # Salida: 7

# Las funciones lambda son especialmente útiles cuando se utilizan 
# como argumentos en funciones de orden superior como `map`, `filter` y `sorted`. 

numeros = [1, 2, 3, 4, 5]
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)  # Salida: [2, 4, 6, 8, 10]

# Estas funciones son ideales para situaciones donde necesitas una función pequeña y temporal


