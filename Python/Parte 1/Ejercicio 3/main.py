peso = input("Ingrese peso en (kg): ")
altura = input("Ingrese altura en (m): ")

imc = float(peso) / float(altura) ** 2

print("Su IMC es: " + str(round(imc,2)) + " kg/m2")
