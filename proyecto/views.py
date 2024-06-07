from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenidos al inicio de Cande")