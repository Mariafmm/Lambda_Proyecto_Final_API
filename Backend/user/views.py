from django.shortcuts import render
from rest_framework.views import APIView   
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import Group, Permission
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import PermissionDenied

def Autenticacion(user, permiso):
    return user.has_rol_perm([permiso]) 

class UserPag(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 20
    
class ListUsers(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = UserPag
    serializer_class = UserSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.role != 4:  # Si no es jefe
            raise PermissionDenied("El usuario no tiene los permisos")
        
        return User.objects.all()

class CrearUsers(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BorrarUsers(APIView): 
    permission_classes=[IsAuthenticated]
    def delete(self, request, pk):
        usuario_id = request.user.id
        usuario = User.objects.get(id=usuario_id)
        if usuario.is_admin: #solo superadmin
            user = User.objects.filter(id=pk).first()  # Buscar la nota manualmente
            if user:  # Verificar si la nota existe
                user.delete()
                return Response({"message": "Usuario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message": "Usuario no existe"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Solo se permite para administradores"}, status=status.HTTP_403_FORBIDDEN)
        
class EditarUsers(APIView):
    permission_classes=[IsAuthenticated]
    def patch(self, request, pk):
        usuario = request.user
        if Autenticacion(usuario, 'change_user'):  # Si es True, continúa
            user = User.objects.filter(id=pk).first()
            if user:
                serializer = UserSerializer(user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Usuario no existe"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "El usuario no tiene los permisos"}, status=status.HTTP_403_FORBIDDEN)

# orm
class LoginUser(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            if response.data['access']:
                token= response.data['access']
                email = request.data['email']
                user = User.objects.get(email=email) #el correo no se puede repetir por el Unique de models
                serializer = UserSerializer(user)
                datos = serializer.data
                data={"message": f"¡Bienvenido al sistema {email}!",
                    "token_de_acceso" : token,
                    "datos_de_tu_cuenta" : datos }
                return Response(data, status=status.HTTP_200_OK)
        except:
            data={"message": "Contraseña o correo incorrectos"} 
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

#prueba de que el token devuelva el usuario
class PerfilUsuario(APIView):
    permission_classes = [IsAuthenticated]  # Requiere autenticación

    def get(self, request):
        usuario = request.user
        return Response({
            "id": usuario.id,
            "email": usuario.email,
            "nombre": usuario.first_name,
            "apellido": usuario.last_name
        })

class ListGroupsAndPermissions(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario_id = self.request.user.id
        usuario = User.objects.get(id=usuario_id)
        print(usuario)
        if usuario.is_admin:
            grupos = Group.objects.all()
            data = []

            for grupo in grupos:
                permisos = grupo.permissions.values("id", "name", "codename")
                data.append({
                    "id": grupo.id,
                    "nombre": grupo.name,
                    "permisos": list(permisos)
                })

            return Response(data, status=200)
        else:
            return Response({"message": "El usuario no tiene los permisos"}, status=status.HTTP_403_FORBIDDEN)

class CreateGroup(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        usuario_id = self.request.user.id
        usuario = User.objects.get(id=usuario_id)
        if usuario.is_admin:
            group_name = request.data.get("name")
            permissions_codenames = request.data.get("permissions", [])

            if not group_name:
                return Response({"error": "El nombre del grupo es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)

            # Crear el grupo si no existe
            group, created = Group.objects.get_or_create(name=group_name)

            # Buscar los permisos por codename
            permissions = Permission.objects.filter(codename__in=permissions_codenames)

            if not permissions.exists():
                return Response({"error": "Algunos permisos no existen."}, status=status.HTTP_400_BAD_REQUEST)

            # Asignar permisos al grupo
            group.permissions.set(permissions)

            return Response({"message": f"Grupo '{group_name}' creado y permisos asignados."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "El usuario no tiene los permisos"}, status=status.HTTP_403_FORBIDDEN)