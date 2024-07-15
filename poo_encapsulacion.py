# Encapsulación consiste en proteger los datos de acceso o usos no controlados 
# a atributos y/o metodos. Pueden tener dos estados Públicos o Privados. 
# La definicion privada se logra anteponiendo __ entre la palabra reservada self y el nombre del atributo 
# en los metodos es altes del nombre
class PersonaPublica:
    def __init__ (self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class PersonaPrivada:
    def __init__ (self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
    
    # para poder leer o modificar se usa la nomenclatura get o set respectivamente
    # Get
    def GetNombre(self):
        return self.__nombre
    def GetApellido(self):
        return self.__apellido
    def GetEdad(self):
        return self.__edad
    # Set
    def SetNombre(self, nombre):
        self.__nombre = nombre
    def SetApellido(self, apellido):
        self.__apellido = apellido
    def SetEdad(self, edad):
        self.__edad = edad


publico = PersonaPublica("Andres", "Moreno", 32)
privado = PersonaPrivada("Carmen", "Lorenzo", 1)
print("\nPRIMER EJERCICIO\n")
print("PERSONA PÚBLICA")
print("Nombre: " + publico.nombre)
print("Apellido: " + publico.apellido)
print("Edad: " + str(publico.edad))
print("PERSONA PRIVADA")
print("Nombre: " + privado.GetNombre())
print("Apellido: " + privado.GetApellido())
print("Edad: " + str(privado.GetEdad()))
print("\nModificando valores\n")
publico.apellido = "Moreno Forero"
privado.SetApellido("Lorenzo Lerma")
privado.SetEdad(34)
print("PERSONA PÚBLICA")
print("Nombre: " + publico.nombre)
print("Apellido: " + publico.apellido)
print("Edad: " + str(publico.edad))
print("PERSONA PRIVADA")
print("Nombre: " + privado.GetNombre())
print("Apellido: " + privado.GetApellido())
print("Edad: " + str(privado.GetEdad()))

# Usando metodos privados
class Coordenada:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def GetX(self):
        return self.__x
    def GetY(self):
        return self.__y
    def SetX(self, x):
        self.__x = x
    def SetY(self, y):
        self.__y = y
        
class Cuadrado:
    def __init__(self,v1,v2,v3,v4):
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3
        self.__v4 = v4
    # Metodos privados
    def __MostrarCoordenadaV1(self):
        print(f"({self.__v1.GetX()},{self.__v1.GetY()})")
    def __MostrarCoordenadaV2(self):
        print(f"({self.__v2.GetX()},{self.__v2.GetY()})")
    def __MostrarCoordenadaV3(self):
        print(f"({self.__v3.GetX()},{self.__v3.GetY()})")
    def __MostrarCoordenadaV3(self):
        print(f"({self.__v3.GetX()},{self.__v3.GetY()})")
    def __MostrarCoordenadaV4(self):
        print(f"({self.__v4.GetX()},{self.__v4.GetY()})")
    # Metodo Publico
    def MostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices:")
        self.__MostrarCoordenadaV1()
        self.__MostrarCoordenadaV2()
        self.__MostrarCoordenadaV3()
        self.__MostrarCoordenadaV4()

v1 = Coordenada(1,1)
v2 = Coordenada(4,1)
v3 = Coordenada(4,4)
v4 = Coordenada(1,4)
cuadrado = Cuadrado(v1,v2,v3,v4)
print("\nSEGUNDO EJERCICIO\n")
cuadrado.MostrarVertices()

