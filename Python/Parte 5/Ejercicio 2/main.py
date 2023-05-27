from functools import reduce

def obtener_impares(lista):
    impares = list(filter(lambda x: x % 2 != 0, lista))
    return reduce(lambda x, y: x + y, impares)

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = obtener_impares(mi_lista)
print(resultado)  # Imprime: 25
