from django.shortcuts import render, redirect
from .models import tickets
from .forms import ticketsForm
from aplicaciones.rutas.models import rutas
from aplicaciones.buses.models import buses
from aplicaciones.principal.models import usuarios

# ----------Envia el objeto tiquetes a la vista index-----------#

def tickets_urls(request):
    tiquete = tickets.objects.all()
    route_model = rutas
    bus_model = buses
    usuario = usuarios
    return render(request, "tickets/tickets.html", {
        'tickets': tiquete,
        'rutas': route_model,
        'buses': bus_model,
        'usuarios':usuario
    })
# ----------Tiquetes Create GET / POST-----------#

def insertar_tickets(request):
    if(request.method == 'GET'):
        forms = ticketsForm()
        listado = {
            'form' : forms,
            'titulo': 'Registrar Tiquete',
            'boton': 'Registrar'
        }
    else:
        forms = ticketsForm(request.POST)
        listado = {
            'form': forms,
            'titulo': 'Registrar tickets',
            'boton': 'Registrar'
        }
        if forms.is_valid():
            forms.save()
            return redirect('tickets_urls')
    return render(request, "tickets/Creartickets.html", listado)

# ----------Tiquetes EDIT-----------#

def editar_tickets(request, id):
    tiquete = tickets.objects.get( id = id)
    if (request.method == 'GET'):
        form = ticketsForm(instance = tiquete)
        listado = {
            'form': form,
            'titulo': 'Editar Tiquete',
            'fecha': tickets.fecha,
            'buses_id': tickets.buses_id,
            'rutas_id': tickets.rutas_id,
            'usuarios_id': tickets.usuarios_id,
            'boton': 'Guardar'
        }
    else:
        forms = ticketsForm(request.POST, instance = tiquete)
        listado = {
            'form': forms
        }
        if forms.is_valid():
            forms.save()
            return redirect('tickets_urls')
    return render(request, 'tickets/Creartickets.html', listado)

# ----------Tiquetes DELETE-----------#

def borrar_tickets(request, id):
    tiquete = tickets.objects.get(id = id)
    tiquete.delete()
    return redirect('tickets_urls')

