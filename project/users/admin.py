from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

#Controla como se muestra y gestiona el usuario en Django Admin, con UserAdmin tienes varias 
#funciones predeterminadas de Django para la administración de usuarios
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass