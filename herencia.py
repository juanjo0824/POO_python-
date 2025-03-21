# Clase Persona

class Persona:
    
    # método constructor
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))

class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", self.__Asignaturas)

class Profesor(Persona):
    def __init__(self):
        self.__antigüedad = 0 
        self.__tutorias = ""
        self.__telefono = 0

    def getAntigüedad(self):
        return self.__antigüedad
    
    def setAntigüedad(self, antigüedad):
        self.__antigüedad = antigüedad

    def getTutorias(self):
        return self.__tutorias
    
    def setTutorias(self, tutorias):
        self.__tutorias = tutorias

    def setTeléfono(self, teléfono):
        self.__teléfono = teléfono

    def getTeléfono(self):
        return self.__teléfono
    
    def mostrarProfesor(self):
        print("Profesor")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tAntigüedad: ", self.__antigüedad)
        print("tTutorias: ",self.__tutorias)




# metodo principal
def main():
    alumno = Alumno()
    alumno.setNombre("Juan Jose")
    alumno.setApellidos("Delgado Benitez")
    alumno.setEdad(18)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["Matemáticas", "Tecnología", "Inglés"])
    alumno.mostrarAlumno()

    # profesor

    profesor = Profesor()
    profesor.setNombre("Néstor")
    profesor.setApellidos("Páez Sarmiento")
    profesor.setEdad(25)
    profesor.setAntigüedad(15)
    profesor.setTutorias("[Sistemas 1]")
    profesor.setTeléfono("333 333 3333")
    profesor.mostrarProfesor()

if __name__ == "__main__":
    main()