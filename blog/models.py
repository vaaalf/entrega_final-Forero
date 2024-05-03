from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    contenido = models.TextField(max_length=5000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entradas')
    imagen = models.ImageField(upload_to="entradas")

    def __str__(self) -> str:
        return f"{self.titulo} {self.subtitulo}"


class Comentario(models.Model):
    mensaje = models.TextField(max_length=5000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE, related_name='comentarios_entrada')

    def __str__(self) -> str:
        return f"{self.usuario}: {self.mensaje}"