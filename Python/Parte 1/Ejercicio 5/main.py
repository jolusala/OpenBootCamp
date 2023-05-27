def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True  # Es divisible entre 400, por lo tanto, es bisiesto
            else:
                return False  # No es divisible entre 400, por lo tanto, no es bisiesto
        else:
            return True  # Es divisible entre 4 pero no entre 100, por lo tanto, es bisiesto
    else:
        return False  # No es divisible entre 4, por lo tanto, no es bisiesto

# Ejemplo de uso
anio = 2024
if es_bisiesto(anio):
    print(f"{anio} es un año bisiesto")
else:
    print(f"{anio} no es un año bisiesto")
