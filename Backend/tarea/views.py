from django.shortcuts import render
from rest_framework.views import APIView   
from .serializers import TareaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Tarea
from user.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import PermissionDenied

class TareaPag(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 20
    
def Autenticacion(user, permiso):
    return user.has_rol_perm([permiso]) 

class CrearTarea(APIView):
    permission_classes=[IsAuthenticated]    
    def post(self, request):
        usuario = request.user
        if Autenticacion(usuario, 'add_tarea'):  # Si es True, continúa
            serializer = TareaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "El usuario no tiene los permisos"}, status=status.HTTP_403_FORBIDDEN)
    
class ListTarea(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = TareaPag
    serializer_class = TareaSerializer
    def get_queryset(self):
        usuario = self.request.user
        if not Autenticacion(usuario, 'view_tarea'):  # Si no tiene permiso, lanza error
            raise PermissionDenied("El usuario no tiene los permisos")

        usuario_id = usuario.id  # Ya está en `request.user`, no hace falta obtenerlo de nuevo
        if usuario.is_admin or usuario.role == 4:  # Rol de jefe
            return Tarea.objects.all()  
        else:
            return Tarea.objects.filter(asignado_a_id=usuario_id, estado=False)


class ModificarTarea(APIView):
    permission_classes=[IsAuthenticated] 
    def patch(self, request, pk):
        usuario = request.user
        if Autenticacion(usuario, 'change_tarea'):  # Si es True, continúa
            usuario = User.objects.get(id=usuario.id)
            if usuario.is_admin or usuario.role==4: #rol de jefe
                tarea = Tarea.objects.get(id=pk)
            else: #rol de empleado
                tarea = Tarea.objects.get(id=pk, asignado_a = usuario.id)
            if tarea:
                serializer = TareaSerializer(tarea, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "La tarea no existe"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "El usuario no tiene los permisos"}, status=status.HTTP_403_FORBIDDEN)