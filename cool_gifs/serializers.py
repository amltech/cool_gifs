from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'src', 'content_type', 'flagged', 'title', 'description', 'height', 'width',)
        read_only_fields = ('content_type', 'height', 'width', )

    def validate_flagged(self, value):
        if not self.instance:
            return value
        if self.instance.flagged and not value:
            raise serializers.ValidationError('Unflagging an image from the API is not permitted')
        return value


class ImageUpdateSerializer(ImageSerializer):
    class Meta(ImageSerializer.Meta):
        read_only_fields = ('content_type', 'height', 'width', 'src',)
