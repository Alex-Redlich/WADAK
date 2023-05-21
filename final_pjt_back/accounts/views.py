from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model


from .models import Chingho
from .serializers import UserSerializer, ChinghoSerializer

# Create your views here.


def signup(request):
    # request.data를 받아와서 돌면서 하기.
    user = get_user_model()
    # request.data 말고 get_user_model의 필드를 도는게 나을듯
    for key in request.data:
        user[key] = request.data.get(key)
        # 유효성 검사하기
        # id 가 중복될경우.

        # 패스워드가 잘못됬을 경우

        # 어쩌구저쩌구
    user.save()
    pass

def login(request):
    # request.user 를 
    pass

def logout(request):
    pass

def update(request, user_pk):
    pass

def delete(request, user_pk):
    pass





def profile(request, user_pk):
    pass

def follow(request, user_pk):
    pass

def review(request, user_pk):
    pass

def like(request, user_pk):
    pass

def profile_update(request, user_pk):
    pass