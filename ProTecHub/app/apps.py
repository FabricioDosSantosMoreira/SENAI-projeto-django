from django.apps import AppConfig
from django.db.utils import IntegrityError, OperationalError


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self) -> None:
        import app.signals
