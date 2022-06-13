from django.urls import path 
from aplicaciones.rutas.views import index, rutas_urls,insertar_rutas,editar_rutas, borrar_rutas

urlpatterns = [

    path('', index, name = "index"),
    path('rutas', rutas_urls , name="rutas_urls"),
    path('insertar_rutas', insertar_rutas, name="insertar_rutas"),
    path('editar_rutas/<int:id>', editar_rutas, name="editar_rutas"),
    path('borrar_rutas/<int:id>', borrar_rutas, name="borrar_rutas"),   
   
]

