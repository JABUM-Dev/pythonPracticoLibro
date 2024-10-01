# Sección 5: Módulos y Paquetes

# Módulos:
# ¿Cómo se importa un módulo en Python? ¿Qué diferencia hay entre import module y from module import function?
# Los modulos se importan al inicio de un programa python con las palabras reservadas import o from modulo import funcion
# la diferencia radica en que import - importa todo el contenido mientras 
# que con from modulo import funcion solo importo lo que necesito 
# lo que a fectos de ahorro de procesamiento es mejor cuando los modulos son my grandes y pesados
# ejemplo
import math  # Importa todo el módulo
print(math.sqrt(16))  # Accede a la función sqrt del módulo math

from math import sqrt  # Solo importa la función sqrt
print(sqrt(16))  # No es necesario usar math. al usar from ... import ...


# Paquetes:
# ¿Qué es un paquete en Python? Explica cómo se organiza un paquete con varios módulos.
#Un paquete es un conjunto de modulos dentro de una carpeta para que 
#python reconozca que es un paquete uno de estos modulos se nombra como __init__.py asi ya no es una simple carpeta
# se organizan segun sus funcionalidades para que todo este ordenado y estructurado.
# por ejemplo un paquete con recetas podria tener el modulo __init__.py, recetas_seco.py, recetas_liquidos.py 
# recetas/         <-- Paquete de recetas
# ├── __init__.py  <-- Indica que es un paquete de Python
# ├── recetas_seco.py
# └── recetas_liquidos.py 
# import recetas  # Importa el paquete, ejecutando cualquier código en __init__.py 
# from recetas import recetas_seco  # Importa solo el módulo 'recetas_seco' del paquete 'recetas'



