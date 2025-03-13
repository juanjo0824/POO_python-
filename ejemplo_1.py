# Clase Persona 

class Persona:

    # método constructor 
    def __init__(self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad 

    # método para mostrar los datos de una persona 
    def MostrarPersona(self):
        print("Nombre: " + self.Nombre)
        print("Apelidos: " + self.Apellidos)
        print("Edad: " + str(self.Edad))

# método principal 
def main():
    p1 = Persona("Juanjo", "Delgado", 18)
    p1.MostrarPersona()
    p2 = Persona("Diego", "Tapias", 17)
    p2.MostrarPersona()
    

if __name__ == "__main__":
    main()