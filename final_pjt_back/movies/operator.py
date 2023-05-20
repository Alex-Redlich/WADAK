from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from .views import get_genres, get_movie_popular, get_movie_recent

def start():
    scheduler=BackgroundScheduler(timezone='Asia/Seoul', max_instances=3)
    # def auto_renewal_movies():
    #     get_genres()
        # get_movie_recent()
        # get_movie_popular()
    scheduler.add_job(get_genres,'interval', seconds = 10, name = 'get_genres')
    scheduler.add_job(get_movie_recent,'interval', days = 1, name = 'get_recet')
    scheduler.add_job(get_movie_popular,'interval', days = 1, name = 'get_popular')
    scheduler.start()