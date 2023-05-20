from django.apps import AppConfig
from django.conf import settings
import django
# from .views import get_genres,get_movie_popular,get_movie_recent

class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'

    def ready(self):

        if settings.SCHEDULER_DEFAULT:
            # django.setup()
            # get_genres()
            
            from . import operator
            operator.start()