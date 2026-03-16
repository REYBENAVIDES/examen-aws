from rest_framework import viewsets
from .models import Imagen
from .serializers import ImagenSerializer

class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all().order_by('-fecha_creacion')
    serializer_class = ImagenSerializer