class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

def crearArchivo():
    archivo = open("vehiculos.txt", "w")
    archivo.close()

def guardarVehiculo(vehiculo):
    archivo = open("vehiculos.txt", "a")
    archivo.write(vehiculo.__str__() + "\n")
    archivo.close()

def leerVehiculos():
    archivo = open("vehiculos.txt", "r")
    print(archivo.read())
    archivo.close()

if __name__=="__main__":
    crearArchivo()

    while True:
        color = input("Ingrese el color del vehiculo (escriba 'salir' para terminar): ")
        if color == "salir":
            leerVehiculos()
            break
        else:
            ruedas = input("Ingrese la cantidad de ruedas del vehiculo: ")
            vehiculo = Vehiculo(color, ruedas)
            guardarVehiculo(vehiculo)
            print("Vehiculo guardado exitosamente!")