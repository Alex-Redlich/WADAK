from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from .views import get_genres, get_movie_popular, get_movie_recent
import datetime


def start():
    scheduler=BackgroundScheduler(timezone='Asia/Seoul', max_instances=5)
    # def auto_renewal_movies():
    #     get_genres()
        # get_movie_recent()
        # get_movie_popular()
    
    scheduler.add_job(get_genres, 'cron', hour=datetime.datetime.today().hour, minute=datetime.datetime.today().minute, second=datetime.datetime.today().second + 2, name = 'get_genres')
    scheduler.add_job(get_movie_recent, 'interval', days = 1, name = 'get_recent')
    scheduler.add_job(get_movie_popular, 'interval', days = 1, name = 'get_popular')
    scheduler.start()