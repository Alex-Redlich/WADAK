from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Chingho(models.Model):
    name = models.CharField(max_length=50)
    is_first = models.BooleanField()
    # 형용사 / 명사 구분
    # is_selected = models.BooleanField(default=False)
    # 선택여부를 중개테이블에서 해야할듯?


class User(AbstractUser):
    followings = models.ManyToManyField('self',symmetrical=False, related_name="followers")
    # 유저 팔로잉
    chinghos = models.ForeignKey(Chingho, on_delete=models.CASCADE, related_name="having_users")
    # 보유 칭호 ; 1:N or m:n...  현재 ~명이 보유중입니다. ?
    today_movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, blank=True)
    # 오늘의 영화
    
    
    is_public = models.BooleanField(default=True)
    # 프로필 공개여부
    
    current_point = models.IntegerField()
    # 보유포인트
    total_point = models.IntegerField()
    # 누적포인트
    level = models.IntegerField()
    # 유저레벨
    rank = models.IntegerField(null=True)
    # 랭킹유저 표시   1 ~ 5위까지 판단.
    
    
    user_id = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    # 
    
    
    profile_pic = models.CharField(max_length=200)
    # 프로필 사진 링크 url

    pass
