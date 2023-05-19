from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie, Genre
from .serializers import MovieSerializer

import requests

headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMGVhNDA4YjMwNGUwZTFkODEwYjVkNzVmNmRlNWE4NiIsInN1YiI6IjYzZDMxOGJlZTcyZmU4MDA4NDkxNmUyNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5S11pzIijwEo4PZ5NR65364akBOW0nkTeQa3ycHXwfs"
    }

# Create your views here.

@api_view(['POST'])
def get_genres(request):
# 서버 구동과 함께 모든 장르를 받아와야함. 처음 한번 가져오기.
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"
    global headers

    response = requests.get(url, headers=headers)
    result = response.json()
    for res in result.get('genres') :
        genre = Genre(
            id = res.get('id'),
            name = res.get('name')
        )
        genre.save()


@api_view(['GET'])
def movie_detail(request, movie_pk):
# 영화 1개 조회
    if Movie.objects.filter(pk=movie_pk):
        movie = Movie.objects.get(pk=movie_pk)
        if movie.get('tagline'):
            serializer = MovieSerializer(movie)
            return Response(serializer)
        
    url = "https://api.themoviedb.org/3/movie/"+ str(movie_pk) +"?language=ko-KR"
    global headers
    response = requests.get(url, headers=headers)
    result = response.json()
    # result type은 dict . dict get 메서드이용해서 필드가 없을 경우 none 입력.
    
    movie = Movie(                
            id = result.get('id'),
            title = result.get('title'),
            overview = result.get('overview'),
            vote_average =  result.get('vote_average'),
            vote_count =  result.get('vote_count'),
            tagline  =  result.get('tagline'),
            backdrop_path =  result.get('backdrop_path'),
            poster_path =  result.get('poster_path'),
            release_date =  result.get('release_datee'),
            runtime =  result.get('runtime'),
            # genres =  result.get('genres'),
            )
    serializer = MovieSerializer(movie)
    movie.save()
    # if serializer.is_valid(raise_exception=True):
        # serializer.save()
        
    return Response(serializer.data)


@api_view(['GET'])
def movie_recent(request):
    # 5페이지까지 불러오기
    url = "https://api.themoviedb.org/3/movie/popular?language=ko-KR&page=1"
    global headers
    
    # ans = 
    pass


def movie_popular(request):
    # 5페이지까지 불러오기
    pass


def movie_ranker(request):
    pass


def movie_friend_like(request, user_pk):
    pass
def movie_friend_today(request, user_pk):
    pass
def movie_friend_review(request, user_pk):
    pass





