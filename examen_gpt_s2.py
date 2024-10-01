# Sección 2: Manejo de Excepciones
# Excepciones:
# ¿Qué es una excepción en Python? Da un ejemplo de cómo manejar una excepción con try-except.
# Una excepción es una forma de controlar errores en el codigo evitando que tenga un cierre inesperado se utiliza el try donde esta el codigo suseptible al error y el except para capturar el error
def division_exacta(numero1, numero2):
    try:
        return numero1 // numero2
    except ZeroDivisionError:  # Capturamos específicamente el error de división por cero
        return "No se puede dividir por 0"
    except TypeError:  # Para el caso de parámetros incorrectos
        return "Parámetro erróneo, verifique e intente nuevamente"
print(division_exacta(4,0))
print(division_exacta(4,'hola'))

# Escribe una función que lea un archivo y capture cualquier excepción si el archivo no se encuentra.
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

leer_txt()

