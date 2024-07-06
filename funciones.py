# Ejercicios propuestos para el tema de funciones
# Funcion basica
def Hola():
    print("¡Hola!, ¿Te esta gustando Python?")
print("Primera invocacion: ", end='')
Hola()
print("Segunda invocacion: ", end='')
Hola()
print('\n')
# Usando return
def HolaReturn():
    return "¡Hola!, ¿Te esta gustando Python?"
print("Primera invocacion: " + HolaReturn())
print("Segunda invocacion: " + HolaReturn())
print('\n')
# Usando parametro de entrada
def ParImpar(param):
    if param % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
numero = int(input("Introduce un número: "))    
ParImpar(numero)
print('\n')
# Usando parametros de entrada
def Multiplicar(pram1, param2):
    return pram1 * param2
multiplicando = int(input("Introduce el multiplicado: "))
multiplicandor = int(input("Introduce el multiplicador: "))
resultado = Multiplicar(multiplicando, multiplicandor)
print("El resultado de la multiplicación es :", resultado)
print('\n')
# Pasando un numero variable de parametros 
def Sumar(*valores):
    resultado = 0 
    for item in valores:
        resultado = resultado + item
    return resultado
resultado = Sumar(3,87,45,63,345,3,58,33,22,11,99)
print("El resultado de la suma es: ", resultado)
print('\n')
# Retornando multiples variables
def SumarMultiplicar(*valores):
    resultado_suma = 0
    resultado_multiplicacion = 1
    for item in valores:
        resultado_suma = resultado_suma + item
        resultado_multiplicacion = resultado_multiplicacion * item
    return resultado_suma, resultado_multiplicacion
ressuma, resmulti = SumarMultiplicar(3,87,45,63,345,3,58,33,22,11,99)
print("El resultado de la suma es: ", ressuma)
print("El resultado  de la multiplicacion es: ", resmulti)
print('\n')

def SumarMultiplicar2(param1, param2):
    return Sumar(param1,param2), Multiplicar(param1, param2)
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
resultado_suma, resultado_multiplicacion = SumarMultiplicar2(numero1, numero2)
print("El resultado de la suma es: ", resultado_suma)
print("El resultado de la multiplicación es: ", resultado_multiplicacion)
print('\n')

# Hacer variables globales dentro de una funcion
def Variables():
    global variable
    print("Valor dentro de la funcion: ", str(variable))
    variable = 3
    print("Valor dentro de la funcion: ", str(variable))
variable = 5
print("Valor en el programa principal: ", str(variable))
Variables()
print("Valor en el programa principal: ", str(variable))
