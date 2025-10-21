from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myApps.usuarios'

    def ready(self):
        import myApps.usuarios.signals
