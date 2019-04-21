from django.apps import AppConfig


class GifStoreConfig(AppConfig):
    name = 'gif_store'

    def ready(self):
        super().ready()
        from . import handlers
