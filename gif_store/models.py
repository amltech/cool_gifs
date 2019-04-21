from django.db import models

class Image(models.Model):

    src = models.ImageField(upload_to='images/%Y/%m/%d/', height_field='height', width_field='width')
    content_type = models.CharField(max_length=255, null=False, default='application/octet-stream', blank=True)
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    flagged = models.BooleanField(default=False)
    height = models.PositiveIntegerField(default=0)
    width = models.PositiveIntegerField(default=0)
