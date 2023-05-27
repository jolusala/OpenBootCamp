import time

hora_actual = time.localtime().tm_hour
minuto_actual = time.localtime().tm_min


if hora_actual >= 19:
    print("Es hora de irnos")
else:
    faltaHora = 18 - hora_actual
    faltaMinuto = 60 - minuto_actual

    print(f"Faltan horas:{faltaHora}")
    print(f"Faltan minutos:{faltaMinuto} ")