from rest_framework import viewsets

from . import serializers
from .models import Image, Tag


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImageSerializer
    queryset = Image.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return serializers.ImageUpdateSerializer
        return super().get_serializer_class()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(image=self.kwargs['image'])
