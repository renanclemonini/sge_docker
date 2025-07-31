from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    # pyrefly: ignore  # bad-override
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
