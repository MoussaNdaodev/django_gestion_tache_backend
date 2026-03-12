from django.apps import AppConfig


class TacheConfig(AppConfig):
    name = 'tache'

    def ready(self):
        import tache.signals  # noqa