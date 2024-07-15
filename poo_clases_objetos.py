class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def MostrarPersona(self):
        print("Nombre: " + self.nombre)
        print("Apellido: " + self.apellido)
        print("Edad: " + str(self.edad))

print("Objetos Originales")
p1 = Persona("Andres", "Mendoza", 32)
p1.MostrarPersona()
p2 = Persona("Nidia", "Peñuela", 31)
p2.MostrarPersona()
print("\n Objetos Modificados")
p2.edad = 33
p1.apellido = "Mendoza Uparela"
p1.MostrarPersona()
p2.MostrarPersona()
print("\n Objetos asignadoa a otro objeto")
p3 = p1
p1.MostrarPersona()
p3.MostrarPersona()
