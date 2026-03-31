from django.apps import AppConfig


class CarsConfig(AppConfig):
    name = 'cars'

    # precisamos fazer isso para informar ao django que nossa aplicação
    # tem signals e o django deve ouvílos
    def ready(self):
        import cars.signals  # noqa
