from django.apps import AppConfig


class UserbioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userbio'
    
    def ready(self):
        import userbio.signals
