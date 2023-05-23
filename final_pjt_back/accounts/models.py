from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Chingho(models.Model):
    name = models.CharField(max_length=50)
    is_first = models.BooleanField()
    having_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="chinghos", through = "Chingho_user")
    # m:n 중개테이블을 만들어야 할듯.
    # 형용사 / 명사 구분
    # is_selected = models.BooleanField(default=False)
    # 선택여부를 중개테이블에서 해야할듯?


class User(AbstractUser):
    followings = models.ManyToManyField('self',symmetrical=False, related_name="followers")
    # 유저 팔로잉
    
    today_movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, null=True)
    # 오늘의 영화
    
    is_public = models.BooleanField(default=True)
    # 프로필 공개여부 정보수정에서만 변경가능하도록
    current_point = models.IntegerField(default=0)
    # 보유포인트
    total_point = models.IntegerField(default=0)
    # 누적포인트
    level = models.IntegerField(default=1)
    # 유저레벨
    rank = models.IntegerField(default=0, null=True)
    # 랭킹유저 표시   1 ~ 5위까지 판단.
    
    nickname = models.CharField(max_length=50)
    intro = models.TextField()
    
    # profile_pic = models.CharField(max_length=200)
    # 프로필 사진 링크 url

class Chingho_user(models.Model):
    chingho = models.ForeignKey('Chingho', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)