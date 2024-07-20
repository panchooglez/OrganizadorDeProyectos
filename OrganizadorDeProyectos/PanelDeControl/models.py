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