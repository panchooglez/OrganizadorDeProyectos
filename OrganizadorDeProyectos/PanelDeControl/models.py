from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'tarea'
        verbose_name_plural = 'tareas'

    def __str__(self):
        return self.descripcion
    
class Despliegue(models.Model):
    titulo = models.CharField(max_length=100, default="")
    desplegada = models.BooleanField(default=False)
    ruta_despliegue = models.CharField(max_length=100, default="")

    class Meta:
        verbose_name = 'despliegue'
        verbose_name_plural = 'despliegues'

    def __str__(self):
        return self.titulo