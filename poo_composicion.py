# Composision consiste en la creacion de nuevas clases 
# a partir de otras clases ya existentes 
# que actuan como elementos compositores de la nueva. 
# Las clases existentes seran atributos de la nueva clase
class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def MostrarCoordenada(self):
        print(f"({self.x},{self.y})")
        
class Cuadrado:
    def __init__(self,v1,v2,v3,v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
    def MostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices:")
        self.v1.MostrarCoordenada()
        self.v2.MostrarCoordenada()
        self.v3.MostrarCoordenada()
        self.v4.MostrarCoordenada()

v1 = Coordenada(1,1)
v2 = Coordenada(4,1)
v3 = Coordenada(4,4)
v4 = Coordenada(1,4)
cuadrado = Cuadrado(v1,v2,v3,v4)
cuadrado.MostrarVertices()
