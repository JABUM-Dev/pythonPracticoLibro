# Modos de apertura de archivos
# "r" Modo lectura - por defecto
# "w" Modo escritura trucado es decir desde cero
# "x" Modo crear fichero y escribir en él
# "a" Modo escritura para un archivo existente con el cursor al final del archivo
# "b" Modo binario
# "t" Modo fichero texto - apertura por defecto
# "+" Modo lectura y escritura

# *Modos Lectura
# Modo lectura archivo completo
"""file = open("fichero.txt", "r")
texto = file.read()
print(texto)
file.close()"""

# Modo lectura linea a linea en un loop
"""for linea in open("fichero.txt","r"):
    print(linea)"""

# Modo lectura linea a linea usando readline()
"""f = open("fichero.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()"""

# Modo lectura completo usando readlines() cada linea queda con indice y se toma como una lista
"""f = open("fichero.txt", "r")
lineas = f.readlines()
f.close()
print(lineas[0])
print(lineas[2])"""

# Tambien podemos convertir directamente a lista el resultante de la lectura
"""f = open("fichero.txt", "r")
lineas = list(f)
f.close()
for linea in lineas:
    print(linea)"""

# *Modos Manipulación
# Manipulacion para escribir final de archivo "a"
"""print("Fichero inicial")
file = open("fichero.txt", "r")
texto = file.read()
file.close()
print (texto)
print("\nInsertando línea\n")
file = open("fichero.txt", "a")
file.write("Nueva linea en el fichero al final usando 'a'")
file.close()
print("\nFichero inicial modificado\n")
file = open("fichero.txt", "r")
texto = file.read()
file.close()
print(texto)"""

# Creacion de fichero y escribir sobre el - si el nombre de archivo ya existe da error
"""file = open("nuevo_fichero.txt", "x")
file.write("Estoy aprendiendo Python\n")
file.write("Me encanta\n")
file.write("Me parece un lenguaje de programacion muy bello\n")
file.close()
print("FICHERO CREADO")
file = open("nuevo_fichero.txt", "r")
texto = file.read()
file.close()
print(texto)"""

# Manipulacion de archivo desde cero usando "w"
file = open("nuevo_fichero.txt", "w")
file.write("Estoy modificando archivos mientas aprendo Python\n")
file.write("Me encanta\n")
file.write("Me parece un lenguaje de programacion muy bello e interesante\n")
file.close()
print("FICHERO RE-ESCRITO")
file = open("nuevo_fichero.txt", "r")
texto = file.read()
file.close()
print(texto)