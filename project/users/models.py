from django.db import models
from django.contrib.auth.models import AbstractUser


# Hereda todos los campos de usuario por defecto en DJANGO
class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
