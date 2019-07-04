import logging

from django import dispatch
from django.db.models import signals

from . import models

logger = logging.getLogger(__name__)


@dispatch.receiver(signals.pre_save, sender=models.Image)
def set_content_type(sender, instance, raw, using, update_fields, **kwargs):
    if instance.content_type:
        return
    try:
        instance.content_type = instance.src.file.content_type
    except (IOError, OSError) as e:
        logger.error('Unable to determine content type of {}:{}'.format(instance.id, e))
