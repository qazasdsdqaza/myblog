from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'
    verbose_name = '用户'

    def ready(self):
        try:
            import user.signals
        except ImportError:
            pass
