from django.apps import AppConfig


class AppmcConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppMC'

    def ready(self):
        import AppMC.signals