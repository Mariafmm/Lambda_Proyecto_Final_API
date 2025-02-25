from django.urls import path
from .views import ListUsers, CrearUsers,BorrarUsers, EditarUsers, LoginUser, PerfilUsuario, ListGroupsAndPermissions,CreateGroup

urlpatterns = [
    path('list/', ListUsers.as_view(), name='lista-users'),
    path('crear/', CrearUsers.as_view(), name='crear-users'),
    path('borrar/<int:pk>/', BorrarUsers.as_view(), name='borrar-users'),
    path('editar/<int:pk>/', EditarUsers.as_view(), name='mod-users'),
    path('login/', LoginUser.as_view(), name="token-users"),
    path('perfil/', PerfilUsuario.as_view(), name="perfil-user"),
    path('list_roles/', ListGroupsAndPermissions.as_view(), name="roles-user"),
    path('crear_roles/', CreateGroup.as_view(), name="crear_roles-user")
    
]