from rest_framework import serializers

from .models import Image, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'label', )


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    permalink = serializers.HyperlinkedIdentityField(
        view_name='permalink', lookup_field='uuid', lookup_url_kwarg='uuid')
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Image
        fields = ('id', 'uuid', 'permalink', 'content_type', 'flagged', 
                  'title', 'description', 'height', 'width', 'src', 'tags')
        read_only_fields = ('uuid', 'content_type', 'height', 'width', 'tags')
    
    def validate_flagged(self, value):
        if not self.instance:
            return value
        if self.instance.flagged and not value:
            raise serializers.ValidationError(
                'Unflagging an image from the API is not permitted')
        return value


class ImageUpdateSerializer(ImageSerializer):
    class Meta(ImageSerializer.Meta):
        read_only_fields = ('content_type', 'height', 'width', 'src', 'tags')
