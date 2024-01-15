from django.apps import AppConfig


class ReceitasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'receitas'

    def ready(self, *args, **kwargs) -> None:
        import receitas.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready
