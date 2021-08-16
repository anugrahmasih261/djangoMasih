from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    # we create this fun for signal.py
    def ready(self):
        import profiles.signals    #after this go to init.py file

