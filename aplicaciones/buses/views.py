from django.shortcuts import render, redirect
from .models import buses
from django.http import HttpResponse
from .forms import busesForm

def index(request):
    return render(request, "index.html", {})

def buses_urls(request):
    buse = buses.objects.all()
    return render(request, "buses/buses.html",{'buses': buse})     

def insertar_buses(request):
    if(request.method == 'GET'):
        forms = busesForm()
    else:
        forms = busesForm(request.POST)   
        if forms.is_valid():
            forms.save()
            return redirect('buses_urls')
    return render(request, 'buses/crearbuses.html' )


def editar_buses(request,id):
    buse = buses.objects.get(id = id)
    if(request.method == 'GET'):
        forms = busesForm(instance= buse)
    else:
        forms = busesForm(request.POST, instance= buse)   
        if forms.is_valid():
            forms.save()
            return redirect('buses_urls')
    return render(request, 'buses/Update_buses.html' )

def borrar_buses(request,id):
    buse = buses.objects.get(id = id)
    buse.delete()
    return redirect('buses_urls')    