from django.urls import path 
from aplicaciones.tickets.views import tickets_urls,insertar_tickets,editar_tickets, borrar_tickets

urlpatterns = [
    path('tickets', tickets_urls , name="principal_urls"),
    path('insertar_tickets', insertar_tickets, name="insertar_tickets"),
    path('editar_tickets/<int:id>', editar_tickets, name="editar_tickets"),
    path('borrar_tickets/<int:id>', borrar_tickets, name="borrar_tickets"),   
   
]

