# Funciones y manejo de diccionarios
dias_semana_ingles = {"Lunes": "Monday",
                      "Martes": "Tuesday",
                      "Miercoles": "Wednesday",
                      "Jueves": "Thursday",
                      "Viernes": "Friday"
                      }
print("Diccionario original: ",dias_semana_ingles)
diccionario_copia = dias_semana_ingles.copy()
print("Diccionario copy:", diccionario_copia)
print("Valor del lunes despues de eliminar: ", dias_semana_ingles.pop("Lunes"))
print("Diccionario despues del pop: ", dias_semana_ingles)
print("Diccionario elemento al azar con popitem: ", dias_semana_ingles.popitem())
print("Valor del Martes (get): ", dias_semana_ingles.get("Martes"))
print("Valor del Lunes (get) (No existe): ", dias_semana_ingles.get("Lunes"))
print("Valor del Lunes (get) (No existe): ", dias_semana_ingles.get("Lunes", "No existe"))
dias_semana_ingles.update({"Lunes": "New_Monday", "Martes": "New_Tuesday"})
print("Diccionario despues de update: ", dias_semana_ingles)
print("setdefault del Sábado: ", dias_semana_ingles.setdefault("Sabado","Saturday"))
print("Diccionario despues del setdefault: ", dias_semana_ingles)
print("setdefault del Lunes: ", dias_semana_ingles.setdefault("Lunes","Monday"))
print("Diccionario despues del setdefault (elemento existente): ", dias_semana_ingles)
print("Elementos iterables (items): ", dias_semana_ingles.items())
print("Elementos iterables (claves): ", dias_semana_ingles.keys())
print("Elementos iterables (valores): ", dias_semana_ingles.values())
