# Create your views here.
from django.shortcuts import render, redirect
from .models import rutas
from django.http import HttpResponse
from .forms import rutasForm

def index(request):
    return render(request, "index.html", {})

def rutas_urls(request):
    ruta = rutas.objects.all()
    return render(request, "rutas/rutas.html",{'rutas': ruta})     

def insertar_rutas(request):
    if(request.method == 'GET'):
        forms = rutasForm()
    else:
        forms = rutasForm(request.POST)   
        if forms.is_valid():
            forms.save()
            return redirect('rutas_urls')
    return render(request, 'rutas/Crearrutas.html' )


def editar_rutas(request,id):
    ruta = rutas.objects.get(id = id)
    if(request.method == 'GET'):
        forms = rutasForm(instance= ruta)
    else:
        forms = rutasForm(request.POST, instance= ruta)   
        if forms.is_valid():
            forms.save()
            return redirect('rutas_urls')
    return render(request, 'rutas/Update_rutas.html' )

def borrar_rutas(request,id):
    ruta = rutas.objects.get(id = id)
    ruta.delete()
    return redirect('rutas_urls')    