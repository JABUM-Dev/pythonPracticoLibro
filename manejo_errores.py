# En este capitulo el libro nos propone ejercicios para aprender a manejar los errores
## Pruebas par aextension Better Comments
# ?Prueba interrogacion
# *Prueba asterisco
# !Prueba admiracion
# todo: prueba con el tag todo
# // prueba comentario con doble barra

print("¡Iniciando programa!")
try:
    print(str(17/0))
except:
    print("ERROR: Division por 0")
else:
    print("INFO: no se han producido errores")    
finally:
    print("¡Primera parte del programa finalizado!")
print("\nComenzando segunda parte del programa")    
try:
    print(str(17/1))
except:
    print("ERROR: Division por 0")
else:
    print("INFO: no se han producido errores")    
finally:
    print("Segunda parte del programa finalizado!")

# Aqui vamos a controlar errores especificos usando a Python
print("\n¡Iniciando programa!\n")
try:
    print(str(17/0))
except ZeroDivisionError:
    print("ERROR: Division por 0")
else:
    print("Controlando error general")
finally:
    print("¡Programa finalizado!")


