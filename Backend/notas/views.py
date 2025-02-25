from .models import Notas, Category
from rest_framework.views import APIView  
from rest_framework.views import APIView   
from .serializers import NotaSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import PermissionDenied

def Autenticacion(user, permiso):
    return user.has_rol_perm([permiso]) 

class NotaPag(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 20
    
class ListNotas(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = NotaPag
    serializer_class = NotaSerializer

    def get_queryset(self):
        usuario = self.request.user
        if not Autenticacion(usuario, 'view_notas'):  # Si no tiene permiso, lanza error
            raise PermissionDenied("El usuario no tiene los permisos")
        
        return Notas.objects.all()

class CrearNotas(APIView):
    permission_classes=[IsAuthenticated]    
    def post(self, request):
        usuario = request.user
        if Autenticacion(usuario, 'add_notas'):  # Si es True, continúa
            serializer = NotaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "El usuario no tiene los permisos"}, status=status.HTTP_403_FORBIDDEN)

class BorrarNotas(APIView):
    permission_classes=[IsAuthenticated]  
    def delete(self, request, pk):
        usuario = request.user
        if Autenticacion(usuario, 'delete_notas'):  # Si es True, continúa
            nota = Notas.objects.filter(id=pk).first() 
            if nota:  
                nota.delete()
                return Response({"message": "Nota eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message": "La nota no existe"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "El usuario no tiene los permisos"}, status=status.HTTP_403_FORBIDDEN)

class ModificarNotas(APIView):
    permission_classes=[IsAuthenticated] 
    def patch(self, request, pk):
        usuario = request.user
        if Autenticacion(usuario, 'change_notas'):  # Si es True, continúa
            nota = Notas.objects.filter(id=pk).first()
            if nota:
                serializer = NotaSerializer(nota, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "La nota no existe"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "El usuario no tiene los permisos"}, status=status.HTTP_403_FORBIDDEN)
    
#categorias
class ListCategoria(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = NotaPag
    serializer_class = CategorySerializer
    def get_queryset(self):
        usuario = self.request.user
        if not Autenticacion(usuario, 'view_category'):  
            raise PermissionDenied("El usuario no tiene los permisos")
        
        return Category.objects.all()

class CrearCategoria(APIView):
    permission_classes=[IsAuthenticated]  
    def post(self, request):
        usuario = request.user
        if Autenticacion(usuario, 'add_category'):  # Si es True, continúa
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "El usuario no tiene los permisos"}, status=status.HTTP_403_FORBIDDEN)
    
class BorrarCateg(APIView):
    permission_classes=[IsAuthenticated] 
    def delete(self, request, pk):
        usuario = request.user
        if Autenticacion(usuario, 'delete_category'):  # Si es True, continúa
            try:
                categ = Category.objects.get(id = pk)  
                categ.delete()
                return Response({"message": "categoria eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({"message": "La categoria no existe"}, status=status.HTTP_404_NOT_FOUND)

class ModificarCateg(APIView):
    permission_classes=[IsAuthenticated] 
    def patch(self, request, pk):
        usuario = request.user
        if Autenticacion(usuario, 'change_category'):  # Si es True, continúa
            categ = Category.objects.get(id = pk)
            if categ:
                serializer = CategorySerializer(categ, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "La categoria no existe"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "El usuario no tiene los permisos"}, status=status.HTTP_403_FORBIDDEN)