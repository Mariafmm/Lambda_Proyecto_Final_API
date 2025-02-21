from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from recordatorios.models import Recordatorio
from .serializers import RecordatorioSerializer
from notas.models import Notas
from tarea.models import Tarea
from .models import Recordatorio
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import PermissionDenied

class RecorPag(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 20
    
def Autenticacion(user, permiso):
    return user.has_rol_perm([permiso]) 

class CrearRecordatorio(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RecordatorioSerializer(data=request.data)
        usuario = self.request.user
        if not Autenticacion(usuario, 'add_recordatorio'):  # Si no tiene permiso, lanza error
            return Response({"error": "El usuario no tiene los permisos"}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            content_type = serializer.validated_data["content_type"]
            contenido_id = serializer.validated_data["contenido_id"]
            usuarios = serializer.validated_data.get("usuarios", [])

            # Validar que el ID exista en el modelo indicado
            model_class = content_type.model_class()
            if not model_class.objects.filter(id=contenido_id).exists():
                return Response(
                    {"error": "El ID especificado no existe en el modelo indicado."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Si "usuarios" está vacío, buscar los usuarios asignados según el tipo de contenido
            if not usuarios:
                if content_type.model == "tarea":
                    try:
                        tarea = Tarea.objects.get(id=contenido_id)
                        usuarios = [tarea.asignado_a]  # Se asigna el usuario de la tarea
                    except Tarea.DoesNotExist:
                        return Response(
                            {"error": "La tarea especificada no existe."},
                            status=status.HTTP_400_BAD_REQUEST
                        )

                elif content_type.model == "notas":
                    try:
                        tareas = Tarea.objects.filter(nota_id=contenido_id)
                        usuarios = list(set(tarea.asignado_a for tarea in tareas))  # Evitar usuarios duplicados
                    except:
                        return Response(
                            {"error": "La nota especificada no existe."},
                            status=status.HTTP_400_BAD_REQUEST
                        )

            # Si aún no hay usuarios, devolver un error
            if not usuarios:
                return Response(
                    {"error": "No hay usuarios asignados a esta nota o tarea."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Crear y asignar usuarios al recordatorio
            recordatorio = serializer.save()
            recordatorio.usuarios.set(usuarios)

            # Serializar la respuesta con los usuarios asignados
            response_data = RecordatorioSerializer(recordatorio).data
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListRecordatorio(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = RecorPag
    serializer_class = RecordatorioSerializer
    def get_queryset(self):
        usuario = self.request.user
        if not Autenticacion(usuario, 'view_recordatorio'):  # Si no tiene permiso, lanza error
            raise PermissionDenied("El usuario no tiene los permisos")
        usuario_id = self.request.user.id
        return Recordatorio.objects.filter(usuarios__id=usuario_id, activo=True)  # Solo los activos
    # def get(self, request):
        # usuario_id = request.user.id
        # recordatorios = Recordatorio.objects.filter(usuarios__id=usuario_id, activo = True) #si activo es False es como un borrado
        # if not recordatorios:
        #     return Response({"message": "No tienes recordatorios"}, status=status.HTTP_200_OK)
        # serializer = RecordatorioSerializer(recordatorios, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

class ModifyRecordatorio(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, pk):
            usuario = self.request.user
            if not Autenticacion(usuario, 'change_recordatorio'):  # Si no tiene permiso, lanza error
                return Response({"error": "El usuario no tiene los permisos"}, status=status.HTTP_400_BAD_REQUEST)
            
            recordatorio = Recordatorio.objects.get(id =pk)
            if recordatorio:
                serializer = RecordatorioSerializer(recordatorio, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "El recordatorio no existe"}, status=status.HTTP_404_NOT_FOUND)