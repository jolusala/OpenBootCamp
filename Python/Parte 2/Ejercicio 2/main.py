class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobar(self):
        if self.nota >= 6:
            return "Si"
        else:
            return "No"

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.nota}, Aprobo: {self.aprobar()}"

def main():
    alumno = Alumno("Jose", 5)
    print(alumno)


if __name__== "__main__":
    main()