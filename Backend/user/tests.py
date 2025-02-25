import sys
import django
import os
 
sys.path.append(r'C:\Users\maria\OneDrive\Documentos\django\dia_1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dia_1.settings')
django.setup()
 
from django.contrib.auth.models import Group, Permission
 
gerente_group = Group.objects.create(name="usuario_n")
 
permisos = Permission.objects.filter(codename__in=["view_contenttype", "change_user", "delete_user"])
 
gerente_group.permissions.set(permisos)
 
print(f"Permisos asignados al grupo {gerente_group.name}: {list(permisos)}")

