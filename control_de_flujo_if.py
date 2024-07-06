# En esta seccion el libro nos propone realizar ejercicios para familiarizarce con el control de flujo IF
numero = int(input("Escriba unnumero del 1 al 1000: "))
if numero < 400:
    print("¡El número que has escrito es menos a 400!")
else:
    print("¡El número que has escrito es mayor o igual a 400!")
print("Has escrito el número " + str(numero))

cadena = input("Introduzca una cadena de texto: ").lower()
if cadena.endswith('a') or cadena.endswith('e') or cadena.endswith('i') or cadena.endswith('o') or cadena.endswith('u'):
    print("¡La cadena de texto acaba en vocal!")
print("Has escrito: " + cadena)

# Anidados
sumando1 = int(input("Escriba el primer sumando: "))
sumando2 = int(input("Escriba el segundo sumando: "))
resultado = sumando1 + sumando2
print("El resultado de la suma es: " + str(resultado))
if resultado % 2 == 0:
    if resultado >= 1000:
        print("¡El resultado de la suma es par y mayor o igual que 1000!")
    else:
        print("¡El resultado de la suma es par y menor que 1000!")
else:
    if resultado >= 1000:
        print("¡El resultado de la suma es impar y mayor o igual que 1000!")
    else:
        print("¡El resultado de la suma es impar y menor que 1000!")

numero1 = int(input("Escriba el primer número: "))
numero2 = int(input("Escriba el segundo número: "))
if numero1 == numero2:
    print("¡Ambos números son igales!")
elif numero1 > numero2:
    print("¡El primer número es mayor que el segundo!")
else:
    print("¡El segundo número es mayor que el primero!")




