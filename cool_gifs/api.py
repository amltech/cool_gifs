from rest_framework import viewsets

from .models import Image
from .serializers import ImageSerializer, ImageUpdateSerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return ImageUpdateSerializer
        return super().get_serializer_class()
