from django.urls import path 
from aplicaciones.buses.views import index, buses_urls,insertar_buses,editar_buses, borrar_buses

urlpatterns = [

    path('', index, name = "index"),
    path('buses', buses_urls , name="buses_urls"),
    path('insertar_buses', insertar_buses, name="insertar_buses"),
    path('editar_buses/<int:id>', editar_buses, name="editar_buses"),
    path('borrar_buses/<int:id>', borrar_buses, name="borrar_buses"),   
   
]

