from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="perfiles", null=True)
    nombre = models.CharField(max_length=300, null=True)
    descripcion = models.TextField(max_length=5000, null=True)
    link = models.URLField(max_length=200, null=True)

    def __str__(self) -> str:
        return f"{self.user} {self.nombre}"