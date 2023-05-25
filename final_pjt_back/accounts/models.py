from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self',symmetrical=False, related_name="followers")
    # 유저 팔로잉
    today_movie = models.ForeignKey('movies.Movie', on_delete=models.SET_NULL, null=True)
    # 오늘의 영화
    
    chingho = models.CharField(max_length=50, default="새싹 유저")
    # 칭호
    is_public = models.BooleanField(default=True)
    # 프로필 공개여부
    current_point = models.IntegerField(default=0)
    # 보유포인트
    total_point = models.IntegerField(default=0)
    # 누적포인트
    level = models.IntegerField(default=1)
    # 유저레벨
    rank = models.IntegerField(default=0, null=True)
    # 랭킹유저 표시   1 ~ 5위까지 판단.
    
    nickname = models.CharField(max_length=50)
    # 닉네임
    intro = models.TextField()
    # 자기소개
    