from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):

    permalink = serializers.HyperlinkedIdentityField(
        view_name='permalink', lookup_field='uuid', lookup_url_kwarg='uuid')

    class Meta:
        model = Image
        fields = ('id', 'uuid', 'permalink', 'content_type', 'flagged', 
                  'title', 'description', 'height', 'width',)
        read_only_fields = ('uuid', 'content_type', 'height', 'width', )

    def validate_flagged(self, value):
        if not self.instance:
            return value
        if self.instance.flagged and not value:
            raise serializers.ValidationError(
                'Unflagging an image from the API is not permitted')
        return value


class ImageUpdateSerializer(ImageSerializer):
    class Meta(ImageSerializer.Meta):
        read_only_fields = ('content_type', 'height', 'width', 'src',)
