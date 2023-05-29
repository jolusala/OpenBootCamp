from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo desde Django")

def despedida(request):
    return HttpResponse("Hasta luego mundo desde Django")

def adulto(request,edad):
    if edad >= 18:
        mensaje = "Eres mayor de edad"
    else:
        mensaje = "Eres menor de edad"
    return HttpResponse(mensaje)