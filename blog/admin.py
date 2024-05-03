from django.contrib import admin

# Register your models here.
from blog import models

# Register your models here.
admin.site.register(models.Entrada)
admin.site.register(models.Comentario)