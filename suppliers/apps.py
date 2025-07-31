from django.apps import AppConfig


class SuppliersConfig(AppConfig):
    # pyrefly: ignore  # bad-override
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suppliers'
