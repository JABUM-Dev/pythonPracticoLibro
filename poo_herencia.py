# La herencia consisten en la definicion de una clase utilizando como base una clase ya existente

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

class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def GetCurso(self):
        return self.__Curso
    def SetCurso(self, curso):
        self.__Curso = curso
    def GetAsignaturas(self):
        return self.__Asignaturas
    def SetAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas
    def MostrarAlumno(self):
        print("Alumno:")
        print("\nNombre:", self.GetNombre())
        print("\nApellido:", self.GetApellido())
        print("\nEdad:", self.GetEdad())
        print("\nCurso:", self.GetCurso())
        print("\nAsignaturas:", self.GetAsignaturas())

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
    def MostrarProfesor(self):
        print("Profesor:")
        print("\nNombre:", self.GetNombre())
        print("\nApellido:", self.GetApellido())
        print("\nEdad:", self.GetEdad())
        print("\nAntigüedad:", self.GetAntiguedad())
        print("\nTutorias:", self.GetTutorias())
        print("\nTelefono:", self.GetTelefono())

alumno = Alumno()
alumno.SetNombre("Andres")
alumno.SetApellido("Mendoza")
alumno.SetEdad("32")
alumno.SetCurso("907B")
alumno.SetAsignaturas(["Python", "Logica I", "Fisica II", "Calculo Multivariado"])
alumno.MostrarAlumno()

profesor = Profesor()
profesor.SetNombre("Moure")
profesor.SetApellido("Dev")
profesor.SetEdad("30")
profesor.SetAntiguedad("20")
profesor.SetTutorias([["Lunes","16-18"],["Jueves", "12-14"],["Viernes", "11-13"]])
profesor.SetTelefono("6584758")
profesor.MostrarProfesor()
