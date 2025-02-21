from django.urls import path
from .views import ListTarea, CrearTarea, ModificarTarea

urlpatterns = [
    path('list/', ListTarea.as_view(), name='lista-notas'),
    path('crear/', CrearTarea.as_view(), name='crear-notas'),
    path('modificar/<int:pk>/', ModificarTarea.as_view(), name='mod-notas'),   
]