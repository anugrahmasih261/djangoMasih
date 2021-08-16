from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sales'
    #after signals.py come here and override it
    def ready(self):
        import sales.signals
