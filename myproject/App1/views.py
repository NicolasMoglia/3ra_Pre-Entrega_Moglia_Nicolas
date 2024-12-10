from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Futbol, Basquet, Usuario, Rugby

# Creo mis vistas.
def inicio(request):
    return render(request, "App1/index.html")

def futbol(request):
    query = request.GET.get("q")
    if query:
        v_fut = Futbol.objects.filter(equipo__icontains=query)
    else:
        v_fut = Futbol.objects.all()
    return render(request, "App1/futbol.html", {"v_fut":v_fut})

def basquet(request):
    return render(request, "App1/basquet.html")

def rugby(request):
    return render(request, "App1/rugby.html")

#Creo formularios para ingresar camisetas
def formulario_futbol(request):
    
    if request.method == "POST":
        futbol_F = Futbol(equipo=request.POST["equipo"],
                        talle=request.POST["talle"],
                        numero=request.POST["numero"])
        futbol_F.save()
        return redirect("")
    else:
        return render(request, "App1/forms/formulario_futbol.html")
    
def formulario_basquet(request):
    
    if request.method == "POST":
        basquet_f = Basquet(equipo=request.POST["equipo"],
                        talle=request.POST["talle"],
                        numero=request.POST["numero"])
        basquet_f.save()
        return redirect("")
    else:
        return render(request, "App1/forms/formulario_basquet.html")
    
def formulario_rugby(request):
    
    if request.method == "POST":
        rugby_f = Rugby(equipo=request.POST["equipo"],
                        talle=request.POST["talle"],
                        numero=request.POST["numero"])
        rugby_f.save()
        return redirect("")
    else:
        return render(request, "App1/forms/formulario_rugby.html")