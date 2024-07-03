# Funciones para string siguiendo el tercer ejercicio del libro
cadena = input("Introduzca una cadena:")
buscar = input("Introduzca una cadena para buscar:")

print("¿Comienza la cadena por la cadena a buscar? (startwith)", cadena.startswith(buscar))
print("¿Termina la cadena por la cadena a buscar? (endswith)", cadena.endswith(buscar))
print("¿Cuantas veces esta la cadena a buscar en cadena? (count)", cadena.count(buscar))

