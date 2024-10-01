# Sección 6: Archivos y Manipulación de Datos

# Archivos:
# Escribe un código para leer un archivo de texto línea por línea.
def leer_txt_linea_linea():
    # Abrimos el archivo en modo lectura
    archivo = open("fichero.txt", "r")
    
    # Leemos todas las líneas en una lista
    lineas = archivo.readlines()

    # Iteramos sobre cada línea y la imprimimos
    for linea in lineas:
        print(linea.strip())  # .strip() elimina los saltos de línea innecesarios al final de cada línea

    archivo.close()  # Cerramos el archivo correctamente
    
leer_txt_linea_linea()

# Explica cómo se cierra un archivo automáticamente usando with open.
# Aprendimos en las secciones anteriores que el with open es una buena practica 
# ya que cierra el archivo asi se presente un error en la ejecucion automaticamente sin afectar el programa
def leer_txt():
    try:
        # Se recomienda usar 'with open' para asegurar el cierre del archivo
        with open("fichero.txt", "r") as file:
            texto = file.read()
            print(texto)
    except FileNotFoundError:  # Capturamos específicamente el error de archivo no encontrado
        print("Error: El archivo no fue encontrado.")
    except Exception as e:  # Capturamos otros errores, si ocurren
        print(f"Ocurrió un error inesperado: {e}")

# Serialización:
# ¿Qué es la serialización en Python? 
# La serializacion en Python es pasar una estructura de datos generalmente listas o tuplas en un formato de texto tipo json para ser leido por este
# ¿Qué módulo se usa para serializar objetos? Da un ejemplo de cómo serializar un diccionario en formato JSON.
# El modulo que se utiliza es pickle pero no se como usarlo ¿ me enseñas ?

import sys

print("This is the name of the program:", sys.argv[0])

print("Argument List:", str(sys.argv))