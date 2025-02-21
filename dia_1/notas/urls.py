from django.urls import path
from .views import ListNotas, CrearNotas, BorrarNotas, ModificarNotas, CrearCategoria, BorrarCateg, ModificarCateg, ListCategoria

urlpatterns = [
    path('list/', ListNotas.as_view(), name='lista-notas'),
    path('crear/', CrearNotas.as_view(), name='crear-notas'),
    path('borrar/<int:pk>/', BorrarNotas.as_view(), name='borrar-notas'),
    path('modificar/<int:pk>/', ModificarNotas.as_view(), name='mod-notas'),
    
    path('list_categoria/', ListCategoria.as_view(), name='lista-categoria'),
    path('crear_categoria/', CrearCategoria.as_view(), name='crear-categoria'),
    path('borrar_categoria/<int:pk>/', BorrarCateg.as_view(), name='borrar-categoria'),
    path('modificar_categoria/<int:pk>/', ModificarCateg.as_view(), name='mod-categoria'),
]