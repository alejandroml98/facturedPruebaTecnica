from django.db import models

# Create your models here.
class Tableros(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'TABLEROS'

class Tareas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    estado = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #Llave foranea con tabla "Tableros"
    id_tablero = models.ForeignKey(Tableros, related_name="tareas", on_delete=models.CASCADE)

    class Meta:
        db_table = 'TAREAS'