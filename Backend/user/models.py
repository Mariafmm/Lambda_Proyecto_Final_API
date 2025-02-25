from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
 
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone,password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico.')
        if not first_name:
            raise ValueError('El usuario debe tener un nombre.')
        if not last_name:
            raise ValueError('El usuario debe tener un apellido.')
 
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone = phone
        )
       
        user.set_password(password)
        user.save()
        return user
 
    def create_superuser(self, email, first_name, last_name, phone, password=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone= phone,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user
 
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=150, verbose_name="Nombres")
    last_name = models.CharField(max_length=255, verbose_name="Apellidos")
    email = models.EmailField(unique=True, db_index=True, verbose_name="Correo electrónico")
    phone = models.CharField(max_length=100, verbose_name="Teléfono")
    status = models.BooleanField(default=False, verbose_name="Estado")
    created_at = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    is_admin = models.BooleanField(default=False, verbose_name="Administrador")
    role = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, default=3, verbose_name="Rol")
   
    reset_password_token = models.CharField(max_length=200, blank=True, null=True, verbose_name="Token de restablecimiento de contraseña")
    reset_password_token_expires_at = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de expiración del token de restablecimiento")
   
    objects = UserManager()
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
 
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
   
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        super(User, self).save(*args, **kwargs)
       
    def create_reset_token(self):
        self.reset_password_token = get_random_string(50)
        self.reset_password_token_expires_at = timezone.now() + timedelta(hours=1)
        self.save()
       
    def has_perm(self, perm, obj=None):
        return True
 
    def has_module_perms(self, app_label):
        return True
    
    def has_rol_perm(self, perms):
        if self.is_admin: #si es super admin
            return True
        userPerms = [p.codename for p in self.role.permissions.all()] #todos los permisos que tenga el rol del usuario
        return any(perm in userPerms for perm in perms) #valida si lo que se entrega esta en la lista de permisos
    
    @property
    def is_staff(self):
        return self.is_admin
   
    class Meta:
        db_table = "users"
 
