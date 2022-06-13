from django.urls import path 
from aplicaciones.principal.views import index, principal_urls,insertar_usuarios,editar_usuarios, borrar_usuarios

urlpatterns = [

    path('', index, name = "index"),
    path('principal', principal_urls , name="principal_urls"),
    path('insertar_usuarios', insertar_usuarios, name="insertar_usuarios"),
    path('editar_usuarios/<int:id>', editar_usuarios, name="editar_usuarios"),
    path('borrar_usuarios/<int:id>', borrar_usuarios, name="borrar_usuarios"),   
   
]

