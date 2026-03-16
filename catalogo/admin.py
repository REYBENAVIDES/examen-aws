from django.contrib import admin
from .models import Imagen

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo_detectado', 'fecha_creacion')
    search_fields = ('nombre', 'tipo_detectado')
