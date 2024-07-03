# Formato de cadenas por operador % 
# %c caracter 
# %s cadenade texto 
# %d numero entero 
# %f numero real 
# %o numero octal 
# %x numero hexadecimal

multiplicando = int(input("Multiplicando:"))
multiplicandor = int(input("Multiplicandor:"))
print("El resultado de multiplicar %d por %d es %d" % (multiplicando, multiplicandor, multiplicando * multiplicandor))

# Formato de cadenas
multiplicando = int(input("Multiplicando:"))
multiplicandor = int(input("Multiplicandor:"))
print("El resultado de multiplicar {0} por {1} es {2}".format(multiplicando, multiplicandor, multiplicando * multiplicandor))

