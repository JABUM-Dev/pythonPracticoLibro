# Una funcion recursiva es aquella que se llama a si misma
def Factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * Factorial(numero - 1)

factorial = int(input("Introduce el número del que quiere calcular el factorial: "))
print("El factorial de " + str(factorial) + " es: " + str(Factorial(factorial)))
