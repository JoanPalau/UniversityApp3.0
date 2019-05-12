from django.apps import AppConfig


class UnivotingConfig(AppConfig):
    name = 'univoting'

    def ready(self):
        import univoting.signals
