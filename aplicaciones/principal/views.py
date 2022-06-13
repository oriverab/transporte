from django.shortcuts import render, redirect
from .models import usuarios
from django.http import HttpResponse
from .forms import usuarioForm

def index(request):
    return render(request, "index.html", {})

def principal_urls(request):
    usuario = usuarios.objects.all()
    return render(request, "Personas/usuarios.html",{'usuarios': usuario})     

def insertar_usuarios(request):
    if(request.method == 'GET'):
        forms = usuarioForm()
    else:
        forms = usuarioForm(request.POST)   
        if forms.is_valid():
            forms.save()
            return redirect('principal_urls')
    return render(request, 'Personas/CrearUsuario.html' )


def editar_usuarios(request,id):
    usuario = usuarios.objects.get(id = id)
    if(request.method == 'GET'):
        forms = usuarioForm(instance= usuario)
    else:
        forms = usuarioForm(request.POST, instance= usuario)   
        if forms.is_valid():
            forms.save()
            return redirect('principal_urls')
    return render(request, 'Personas/Update_users.html' )

def borrar_usuarios(request,id):
    usuario = usuarios.objects.get(id = id)
    usuario.delete()
    return redirect('principal_urls')    