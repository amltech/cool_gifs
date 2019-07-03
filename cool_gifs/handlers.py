import logging

import PIL
from django import dispatch
from django.db.models import signals

from . import models

logger = logging.getLogger(__name__)


@dispatch.receiver(signals.pre_save, sender=models.Image)
def set_content_type(sender, instance, raw, using, update_fields, **kwargs):
    try:
        #with instance.src.open() as src:
        image = PIL.Image.open(instance.src.name)
        instance.content_type = image.format
        image.close()
    except (IOError, OSError):
        logger.error('Unable to determine content type of {}'.format(instance.id))
