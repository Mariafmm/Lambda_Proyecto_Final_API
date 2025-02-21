from django.urls import path
from .views import CrearRecordatorio, ListRecordatorio,ModifyRecordatorio
urlpatterns = [
    path('crear/', CrearRecordatorio.as_view(), name='crear-notif'),
    path('list/', ListRecordatorio.as_view(), name='listar-notif'),
    path('editar/<int:pk>/', ModifyRecordatorio.as_view(), name='editar-notif'),
]