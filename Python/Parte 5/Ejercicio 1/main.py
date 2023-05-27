lista = input("Ingrese paises separados por coma (,): ")
lista = lista.split(",")
lista = set(lista)
lista = list(lista)
lista = sorted(lista)

for i in lista:
    print(i+",")
