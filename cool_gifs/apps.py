from django.apps import AppConfig


class CoolGifsConfig(AppConfig):
    name = 'cool_gifs'

    def ready(self):
        super().ready()
        from . import handlers
