from django.db import models

class Imagen(models.Model):
    nombre = models.CharField(max_length=255)
    tipo_detectado = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    archivo = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
