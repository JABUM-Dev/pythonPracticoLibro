# La tecnica de la herencia multiple permite heredar de mas de una clase

class Persona():
    def __init__(self):
        self.__Nombre = ""
        self.__Apellido = ""
        self.__Edad = 0
    
    def GetNombre(self):
        return self.__Nombre
    def SetNombre(self, nombre):
        self.__Nombre = nombre
    def GetApellido(self):
        return self.__Apellido
    def SetApellido(self, apellido):
        self.__Apellido = apellido
    def GetEdad(self):
        return self.__Edad
    def SetEdad(self, edad):
        self.__Edad = edad

class Profesor(Persona):
    def __init__(self):
        self.__Antiguedad = ""
        self.__Tutorias = ""
        self.__Telefono = ""
    
    def GetAntiguedad(self):
        return self.__Antiguedad
    def SetAntiguedad(self, antiguedad):
        self.__Antiguedad = antiguedad
    def GetTutorias(self):
        return self.__Tutorias
    def SetTutorias(self, tutorias):
        self.__Tutorias = tutorias
    def GetTelefono(self):
        return self.__Telefono
    def SetTelefono(self, telefono):
        self.__Telefono = telefono

class Investigador(Persona):
    def __init__(self):
        self.__Especialidad = ""
        self.__Años = ""
    
    def GetEspecialidad(self):
        return self.__Especialidad
    def SetEspecialidad(self, especialidad):
        self.__Especialidad = especialidad
    def GetAños(self):
        return self.__Años
    def SetAños(self, años):
        self.__Años = años

class ProfesorUniversitario(Profesor, Investigador):
    def __init__(self):
        self.__Universidad = ""
        self.__Departamento = ""
    def GetUniversidad(self):
        return self.__Universidad
    def SetUniversidad(self, universidad):
        self.__Universidad = universidad
    def GetDepartamento(self):
        return self.__Departamento
    def SetDepartamento(self, departamento):
        self.__Departamento = departamento
    def MostrarProfesorUniversitario(self):
        print("Profesor Universitario:")
        print("\nNombre:", self.GetNombre())
        print("\nApellido:", self.GetApellido())
        print("\nEdad:", self.GetEdad())
        print("\nAntigüedad:", self.GetAntiguedad())
        print("\nTutorias:", self.GetTutorias())
        print("\nTelefono:", self.GetTelefono())
        print("\nEspecialidad:", self.GetEspecialidad())
        print("\nAños:", self.GetAños())
        print("\nUniversidad:", self.GetUniversidad())
        print("\nDepartamento:", self.GetDepartamento())

profesor = ProfesorUniversitario()
profesor.SetNombre("Moure")
profesor.SetApellido("Dev")
profesor.SetEdad("30")
profesor.SetAntiguedad("20")
profesor.SetTutorias([["Lunes","16-18"],["Jueves", "12-14"],["Viernes", "11-13"]])
profesor.SetTelefono("6584758")
profesor.SetEspecialidad("Desarrollo de Software")
profesor.SetAños("15")
profesor.SetUniversidad("Universidad de Alicante")
profesor.SetDepartamento("Lenguajes y Sistemas Informaticos")
profesor.MostrarProfesorUniversitario()


