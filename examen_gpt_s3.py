# Sección 3: Clases y Programación Orientada a Objetos (POO)

# Clases y Objetos:
# Crea una clase llamada Coche que tenga atributos como marca, modelo y color. Incluye un método que imprima la descripción del coche.
class Vehiculo:
    total_coches = 0

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        Vehiculo.total_coches += 1  # Incrementa el contador de coches creados
    
    def descripcion_coche(self):
        return f"El coche es marca {self.marca}, modelo {self.modelo} de color {self.color}"
    
    @classmethod
    def coches_creados(cls):
        return f"Se han creado {cls.total_coches} coches en total."

# Explica la diferencia entre un método de instancia y un método de clase. Da un ejemplo de ambos.
# Un método de instancia es un método que trabaja con una instancia específica de una clase, 
# accediendo a sus atributos y realizando acciones sobre esa instancia. El método descripcion_coche es un ejemplo de un método de instancia.
mi_coche = Vehiculo('Chevrolet', 2016, 'Gris Ocaso')
print(mi_coche.descripcion_coche())
# un metodo de clase Estos métodos operan a nivel de clase, no de instancia, 
# y se definen usando el decorador @classmethod. Se pasan la clase como el primer argumento, convencionalmente llamado cls.
print(Vehiculo.coches_creados())  # Llamada al método de clase

# Herencia:
# Crea una clase Vehiculo y hereda de ella la clase Coche. Asegúrate de que la clase Coche herede un método de la clase Vehiculo.
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, familia):
        super().__init__(marca, modelo, color)
        self.__familia = None
        self.familia = familia
    
    @property
    def familia(self):
        return self.__familia
    
    @familia.setter
    def familia(self, familia):
        self.__familia = familia

# Heredando de Coche puedo instanciar con el metodo init mi_vehiculo y agregar mis atributos de clase particulares
mi_vehiculo = Coche('Chevrolet', 2016, 'Gris Ocaso', 'Spark GT')
# Heredando de Coche puedo heredar el metodo descripcion_coche
print(mi_vehiculo.descripcion_coche())

# Métodos y atributos privados:
# Explica la diferencia entre un atributo público y uno privado. ¿Cómo se define un atributo privado en Python?
# un atributo público es aquel que permite ser accedido desde fuera de la clase 
# un atributo privado en Python es una convencion usando el guion al piso o doble guion al piso __ para evitar se accedido o modificado desde afuera de la clase sin usar getter o setter
# como ejemplo cree a proposito el atributo __familia el cual es privado y solo puede ser modificado por la propiedad setter @familia.setter
