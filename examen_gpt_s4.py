# Sección 4: Decoradores, Generadores y Comprensiones
# Decoradores:
# ¿Qué es un decorador en Python? Da un ejemplo de un decorador que imprima un mensaje antes y después de ejecutar una función.
# un decorador es una funcion que envuelve a otra y le da un comportamiento 
# diferente al estabelcer ciertos pasos antes o despues de la ejecucion del mismo se identifican porque se utiliza un @ al inicio de sus nombres
def decorando(funcion):
    def multiplica_decorado(numero1, numero2):
        print("Bienvenido, vamos a multiplicar")  # Se ejecuta antes de la función original
        total = funcion(numero1, numero2)         # Se ejecuta la función original
        print("Se ha ejecutado la multiplicación")  # Se ejecuta después de la función original
        return total
    return multiplica_decorado

@decorando
def multiplica(numero1, numero2):
    print("Entra en multiplica")
    return numero1 * numero2

# Llamada a la función decorada
print(multiplica(9, 9))


# Generadores:
# ¿Qué son los generadores en Python? Escribe un generador que devuelva los primeros 5 números pares.
# Los generadores son capaces de mantener un estado variable en memoria por solicitud se 
# identifican con la palabra reservada yield y son capaces de mantener el resultado hasta ser llamados nuevamente
# tengo claro el concepto pero no se hacerlo

def numeros_pares():
    numero = 0  # Inicializamos el número
    while numero <= 10:  # Queremos generar los primeros 5 números pares (0, 2, 4, 6, 8, 10)
        yield numero
        numero += 2  # Incrementamos de 2 en 2

# Usamos el generador para obtener los números
generador_pares = numeros_pares()

# Imprimimos los primeros 5 números pares
for _ in range(5):
    print(next(generador_pares))

# Comprensión de Diccionarios:
# Escribe una comprensión de diccionario que convierta una lista de números en un diccionario, 
# donde la clave sea el número y el valor sea el cuadrado del número.

lista_numeros = [1,2,3,4,5,6,7,8,9]
diccionario_numeros = {x : x ** 2 for x in lista_numeros}
print(diccionario_numeros)
