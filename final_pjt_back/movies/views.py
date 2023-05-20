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


def overview_is_valid(overview):
    # 줄거리에 19금 단어 포함이라면 삭제
    # overview = Movie.get("overview")
    filterwords = ["쾌락","욕망","남근","처제","에로"]
    for filterword in filterwords:
        if filterword in overview:
            movie = Movie.objects.get(overview = overview)
            movie.delete()
            return False
    return True


# Create your views here.

@api_view(['GET','POST'])
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
    
    return Response({'status':'success'})


@api_view(['GET'])
def get_movie_recent(request):
    # 서버 시작과 동시에 5페이지까지 불러오기  & ap 스케쥴러로 24시간 마다 한번 불러오기
    base_url = "https://api.themoviedb.org/3/movie/upcoming?language=ko-KR&page="
    global headers
    for i in ["1","2","3","4","5"]:
        url = base_url + i
        response = requests.get(url, headers=headers)
        result_list = response.json()
        
        for result in result_list.get("results"):
            movie = Movie(                
                    id = result.get('id'),
                    title = result.get('title'),
                    overview = result.get('overview'),
                    popularity = result.get('popularity'),
                    vote_average =  result.get('vote_average'),
                    vote_count =  result.get('vote_count'),
                    tagline  =  result.get('tagline'),
                    backdrop_path =  result.get('backdrop_path'),
                    poster_path =  result.get('poster_path'),
                    release_date =  result.get('release_date'),
                    runtime =  result.get('runtime'),
                    # test = True
                    # genres =  result.get('genres'),
                    )
            movie.save()
            
            for genre_id in result.get('genre_ids'):
                genre = Genre.objects.get(id=genre_id)
                movie.genres.add(genre)
            
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_movie_popular(request):
    # 서버 시작과 동시에 5페이지까지 불러오기  & ap 스케쥴러로 24시간 마다 한번 불러오기
    base_url = "https://api.themoviedb.org/3/movie/popular?language=ko-KR&page="
    global headers
    for i in ["1","2","3","4","5"]:
        url = base_url + i
        response = requests.get(url, headers=headers)
        result_list = response.json()
        for result in result_list.get("results"):
            
            movie = Movie(                
                    id = result.get('id'),
                    title = result.get('title'),
                    overview = result.get('overview'),
                    popularity = result.get('popularity'),
                    vote_average =  result.get('vote_average'),
                    vote_count =  result.get('vote_count'),
                    tagline  =  result.get('tagline'),
                    backdrop_path =  result.get('backdrop_path'),
                    poster_path =  result.get('poster_path'),
                    release_date =  result.get('release_date'),
                    runtime =  result.get('runtime'),
                    # genres =  result.get('genres'),
                    )
            movie.save()
            
            for genre_id in result.get('genre_ids'):
                genre = Genre.objects.get(id=genre_id)
                movie.genres.add(genre)
                
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies,many=True)
    return Response(serializer.data)


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
            popularity = result.get('popularity'),
            vote_average =  result.get('vote_average'),
            vote_count =  result.get('vote_count'),
            tagline  =  result.get('tagline'),
            backdrop_path =  result.get('backdrop_path'),
            poster_path =  result.get('poster_path'),
            release_date =  result.get('release_date'),
            runtime =  result.get('runtime'),
            # genres =  result.get('genre_ids'),
            )
    movie.save()
    for genredict in result.get('genres'):
        genre = Genre.objects.get(pk=genredict.ger('id'))

        movie.genres.add(genre)

    
    serializer = MovieSerializer(movie)
    # if serializer.is_valid(raise_exception=True):
        # serializer.save()
        
    return Response(serializer.data)





def movie_ranker(request):
    pass


def movie_friend_like(request, user_pk):
    pass
def movie_friend_today(request, user_pk):
    pass
def movie_friend_review(request, user_pk):
    pass





