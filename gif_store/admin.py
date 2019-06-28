from django.contrib import admin
from django.utils import timezone

from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_time'
    list_display = ('id', 'title', 'flagged', 'creation_time', 'last_modified')
    list_filter = ('flagged', )
    readonly_fields = ('height', 'width', 'src', 'content_type')

    actions = ['flag_image', 'unflag_image']

    def flag_image(self, request, queryset):
        queryset.update(flagged=True, last_modified=timezone.now())
    flag_image.short_description = 'Mark selected images as flagged.'

    def unflag_image(self, request, queryset):
        queryset.update(flagged=False, last_modified=timezone.now())
    unflag_image.short_description = 'Mark selected images as not flagged.'

