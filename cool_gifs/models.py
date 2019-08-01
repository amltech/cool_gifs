import uuid

from django.db import models


class Image(models.Model):

    uuid = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=False)
    src = models.ImageField(
        upload_to='images/%Y/%m/%d/', 
        height_field='height', 
        width_field='width')
    content_type = models.CharField(
        max_length=255, null=False, default='', blank=True)
    title = models.CharField(
        max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    flagged = models.BooleanField(default=False)
    height = models.PositiveIntegerField(default=0)
    width = models.PositiveIntegerField(default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.uuid)


class Tag(models.Model):
    image = models.ForeignKey(Image, null=False, on_delete=models.CASCADE)
    label = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return '{}:{}'.format(self.image.uuid, self.label)
