from rest_framework import filters, viewsets

from . import serializers
from .models import Image, Tag


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImageSerializer
    queryset = Image.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'tags__label']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('tags')

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

    def perform_create(self, serializer):
        serializer.save(image_id=self.kwargs['image'])
