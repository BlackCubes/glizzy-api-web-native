from django.apps import AppConfig


class GlizzyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "glizzy"

    def ready(self):
        from . import signals
