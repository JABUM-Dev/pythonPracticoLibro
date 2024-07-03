# Funciones con cadenas de texto segundo ejercicio del libro
cadena = input("Introduzca una cadena cib espacios al principio y al final:")

print("Longitud cadena:", len(cadena))
cadenalstrip = cadena.lstrip()
print("Cadena (lstrip) agregandole un punto final:", cadenalstrip,end='.')
print("\nLongitud de la cadena (lstrip):", len(cadenalstrip))
cadenarstrip = cadena.rstrip()
print("Cadena (rstrip) agregando un punto final:", cadenarstrip,end='.')
print("\nLongitud de la cadena (rstrip):", len(cadenarstrip))
cadenastrip = cadena.strip()
print("Cadena (strip) agregando un punto final:", cadenastrip,end='.')
print("\nLongitud de la cadena (strip):", len(cadenastrip))

