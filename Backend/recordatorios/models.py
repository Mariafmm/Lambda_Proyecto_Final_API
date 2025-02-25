from django.db import models
from user.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Recordatorio(models.Model):
    fecha_recordatorio = models.DateTimeField()  
    activo = models.BooleanField(default=True)
    usuarios = models.ManyToManyField(User, related_name="recordatorios")  # Asignar usuarios
    # Relación Genérica para que funcione con Notas o Tareas
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #notas o tarea
    contenido_id = models.PositiveIntegerField() #id de la nota o de la tarea
    contenido = GenericForeignKey('content_type', 'contenido_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Recordatorio para {self.contenido} el {self.fecha_recordatorio}"

# para crear recordatorio
# from django.contrib.contenttypes.models import ContentType
# from user.models import User
# from notas.models import Notas
# from recordatorios.models import Recordatorio
# from datetime import datetime

# usuario = User.objects.get(username="Juan")  # Usuario al que pertenece el recordatorio
# nota = Notas.objects.get(id=1)  # La nota asociada

# recordatorio = Recordatorio.objects.create(
#     usuario=usuario,
#     fecha_recordatorio=datetime(2025, 3, 10, 14, 30),  # 10 de marzo de 2025 a las 14:30
#     debe_notificar=True,
#     content_type=ContentType.objects.get_for_model(nota),
#     object_id=nota.id
# )
# obtener las activas
# from datetime import datetime
# from django.utils.timezone import now
# from recordatorios.models import Recordatorio

# # Obtener la fecha actual
# hoy = now().date()

# # Filtrar recordatorios del día de hoy con `debe_notificar=True`
# recordatorios_hoy = Recordatorio.objects.filter(
#     fecha_recordatorio__date=hoy,
#     debe_notificar=True
# )

# # Mostrar resultados
# for recordatorio in recordatorios_hoy:
#     print(recordatorio)