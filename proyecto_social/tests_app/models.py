from django.db import models

# Create your models here.
class Test(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Pregunta(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="preguntas")
    pregunta = models.CharField(max_length=500)

