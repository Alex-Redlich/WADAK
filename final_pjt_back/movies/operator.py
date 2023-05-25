from apscheduler.schedulers.background import BackgroundScheduler
from .views import get_genres, get_movie_popular, get_movie_recent
from accounts.views import rank_renewal
import datetime


def start():
    scheduler=BackgroundScheduler(timezone='Asia/Seoul', max_instances=30)

    activated_time = datetime.datetime.today()
    
    # scheduler.add_job(rank_renewal, 'cron', hour=activated_time.hour, minute=activated_time.minute, second=activated_time.second + 2, name = 'rank_renewal')
    # scheduler.add_job(get_genres, 'cron', hour=activated_time.hour, minute=activated_time.minute, second=activated_time.second + 2, name = 'get_genres')
    # scheduler.add_job(get_movie_recent, 'cron', hour = activated_time.hour, minute=activated_time.minute, second=activated_time.second + 4, name = 'get_recent')
    # scheduler.add_job(get_movie_popular, 'cron', hour=activated_time.hour, minute=activated_time.minute, second=activated_time.second + 10, name = 'get_popular')
    
    scheduler.start()