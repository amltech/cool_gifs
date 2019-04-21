from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'src', 'content_type', 'flagged', 'title', 'description', 'height', 'width',)
        read_only_fields = ('content_type', 'height', 'width', )
