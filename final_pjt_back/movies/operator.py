from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import register_events, DjangoJobStore
from .views import get_genres, get_movie_popular, get_movie_recent
import datetime


def start():
    scheduler=BackgroundScheduler(timezone='Asia/Seoul', max_instances=7)
    # def auto_renewal_movies():
    #     get_genres()
        # get_movie_recent()
        # get_movie_popular()
    activated_time = datetime.datetime.today()
    
    
    # scheduler.add_job(get_genres, 'cron', hour=activated_time.hour, minute=activated_time.minute, second=activated_time.second + 2, name = 'get_genres')
    # scheduler.add_job(get_movie_recent, 'cron', hour = activated_time.hour, minute=activated_time.minute, second=activated_time.second + 4, name = 'get_recent')
    # scheduler.add_job(get_movie_popular, 'cron', hour=activated_time.hour, minute=activated_time.minute, second=activated_time.second + 10, name = 'get_popular')
    
    
    scheduler.start()