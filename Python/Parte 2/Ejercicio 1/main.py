class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return f"Color: {self.color}\nRuedas: {self.ruedas}\nPuertas: {self.puertas}"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}\nVelocidad: {self.velocidad}\nCilindrada: {self.cilindrada}"

def main():
    coche = Coche("Rojo", 4, 2, 120, 1600)
    print(coche)

if __name__ == "__main__":
    main()