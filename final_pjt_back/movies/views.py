from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie, Genre
from .serializers import MovieSerializer, MovieSimpleSerializer
from accounts.models import User
from accounts.serializers import UserSerializer
import requests
import random

headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMGVhNDA4YjMwNGUwZTFkODEwYjVkNzVmNmRlNWE4NiIsInN1YiI6IjYzZDMxOGJlZTcyZmU4MDA4NDkxNmUyNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5S11pzIijwEo4PZ5NR65364akBOW0nkTeQa3ycHXwfs"
    }

# def test_func(request):
#     test_queryset = test.objects.order_by('-created_at')
#     filtered_queryset = test_queryset.filter(genre_id=12)
#     movie_queryset = Movie.objects.filter(test__in=filtered_queryset).order_by('-test__created_at')

#     for movie in movie_queryset:
#         print(movie.title)
    # filter(test.movie.id < "100").order_by('test.movie')
    
    # return movie_queryset

@api_view(['GET'])
def ranker_today_movie(request):
    # 랜덤 랭커 유저의 칭호, 닉네임, todaymovie_id
    rankers = User.objects.filter(rank__gt=0, is_public__gt = 0, today_movie__isnull=False)
    ranker = random.choice(rankers)
    movie = ranker.today_movie
    
    
    data = {
        'ranker_nickname' : ranker.nickname, 
        'chingho' : ranker.chingho
        }
    
    serializer = MovieSimpleSerializer(movie)
    data.update(serializer.data)
    
    return Response(data)
    # {ranker_nickname, id, title}

@api_view(['GET'])
def follow_today_movie(request):
    # 팔로잉 랜덤유저 1명 닉네임, movie_detail 전체 정보
    user = User.objects.get(pk = request.data.get("user_pk"))
    random_following = random.choice(user.followings.filter(today_movie__isnull=False, is_public__gt = 0))
    movie = random_following.today_movie
    
    data = {'following_nickname' : random_following.nickname}
    serializer = MovieSerializer(movie)
    data.update(serializer.data)
    
    return Response(data)
    # { following_nickname , id, title, ...}

@api_view(['GET'])
def follow_like_movie(request):
    #  팔로잉 랜덤유저 1명 닉네임, 최근 좋아요한 영화 id & path 3개
    user = User.objects.get(pk = request.data.get("user_pk"))
    followings = user.followings.filter(is_public__gt = 0)
    random_following = random.choice(followings)
    
    while random_following.like_movies.count() == 0:
        random_following = random.choice(followings)
    movies = random_following.like_movies.all().order_by('-Movie_like_users__created_at')[:3]
    
    data = {'following_nickname' : random_following.nickname}
    serializer = MovieSimpleSerializer(movies, many = True)
    data.update(movies = serializer.data)
    
    return Response(data)
    # {following_nickname , movies }

@api_view(['GET'])
def follow_review_movie(request):
    # 팔로잉 랜덤유저 1명 닉네임, 최근 리뷰 남긴 영화 id & path 3개
    user = User.objects.get(pk = request.data.get("user_pk"))
    followings = user.followings.filter(is_public__gt = 0)
    random_following = random.choice(followings)
    
    while random_following.reviews.count() == 0:
        random_following = random.choice(followings)
    reviews = random_following.reviews.all().order_by('-review__created_at')[:10]
    review_ids = list(set([review.id for review in reviews]))
    movies = Movie.objects.filter(review__in=review_ids)[:3]
    
    data = {'following_nickname' : random_following.nickname}
    serializer = MovieSimpleSerializer(movies, many = True)
    data.update(movies = serializer.data)
    
    return Response(data)
    # {following_nickname , movies }

@api_view(['GET'])
def popular_movie(request):
    # popularity로 movie 정렬 후 5개 출력
    movies = Movie.objects.order_by('-popularity')[:5]
    serializer = MovieSimpleSerializer(movies, many = True)
    # serializer.data => list안에 들어감.
    return Response(serializer.data)
    # [ {} , {}, {}]

    # data = {'following_nickname' : 'ㅁ'}
    # movies = Movie.objects.get(id=175)
    # serializer = MovieSerializer(movies)
    # data.update(serializer.data)
    # # serializer.data => list안에 들어감.
    # return Response(data)

@api_view(['GET'])
def recent_movie(request):
    # 개봉일로 정렬 후 5개 출력
    movies = Movie.objects.order_by('-release_date')[:5]
    serializer = MovieSimpleSerializer(movies, many = True)
    return Response(serializer.data)
    # [ {} , {}, {}]





def overview_is_valid(overview):
    # 줄거리에 19금 단어 포함이라면 거르기.
    # overview = Movie.get("overview")
    filterwords = ["쾌락","욕망","남근","처제","에로","형수","sex"]
    for filterword in filterwords:
        if filterword in overview:
            # movie = Movie.objects.get(overview = overview)
            # movie.delete()
            return False
    return True


# Create your views here.
# follower ~ 누구가 

def get_genres():
# 서버 구동과 함께 모든 장르를 받아와야함. 처음 한번 가져오기.
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"
    global headers
    # print("장르~")
    response = requests.get(url, headers=headers)
    result = response.json()
    for res in result.get('genres') :
        genre = Genre(
            id = res.get('id'),
            name = res.get('name')
        )
        genre.save()
    
    return Response({'status':'success'})

def get_movie_recent():
    # 서버 시작과 동시에 5페이지까지 불러오기  & ap 스케쥴러로 24시간 마다 한번 불러오기
    base_url = "https://api.themoviedb.org/3/movie/upcoming?language=ko-KR&page="
    global headers
    # print("recent~")
    for i in ["1","2","3","4","5"]:
        url = base_url + i
        response = requests.get(url, headers=headers)
        result_list = response.json()
        
        for result in result_list.get("results"):
            if overview_is_valid(result.get('overview')):
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

def get_movie_popular():
    # 서버 시작과 동시에 5페이지까지 불러오기  & ap 스케쥴러로 24시간 마다 한번 불러오기
    base_url = "https://api.themoviedb.org/3/movie/popular?language=ko-KR&page="
    global headers
    # print("파퓰라~")
    for i in ["1","2","3","4","5"]:
        url = base_url + i
        response = requests.get(url, headers=headers)
        result_list = response.json()
        for result in result_list.get("results"):
            if overview_is_valid(result.get('overview')):
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
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_search(request, keyword):
    # FE로 json 자료만 보내줌
    url ="https://api.themoviedb.org/3/search/movie?query="+ keyword +"&include_adult=false&language=ko-KR&page=1"
    global headers
    
    response = requests.get(url, headers=headers)
    result_list = response.json()

    # for result in result_list.get("results"):
        
    #     movie = Movie(                
    #             id = result.get('id'),
    #             title = result.get('title'),
    #             overview = result.get('overview'),
    #             popularity = result.get('popularity'),
    #             vote_average =  result.get('vote_average'),
    #             vote_count =  result.get('vote_count'),
    #             tagline  =  result.get('tagline'),
    #             backdrop_path =  result.get('backdrop_path'),
    #             poster_path =  result.get('poster_path'),
    #             release_date =  result.get('release_date'),
    #             runtime =  result.get('runtime'),
    #             # genres =  result.get('genres'),
    #             )
    #     movie.save()
        
    #     for genre_id in result.get('genre_ids'):
    #         genre = Genre.objects.get(id=genre_id)
    #         movie.genres.add(genre)
    
    return Response(result_list)

@api_view(['GET'])
def movie_detail(request, movie_pk):
# 영화 1개 조회
    if Movie.objects.filter(pk=movie_pk):
        movie = Movie.objects.get(pk=movie_pk)
        if movie.tagline:
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        
    url = "https://api.themoviedb.org/3/movie/"+ str(movie_pk) +"?language=ko-KR"
    global headers
    response = requests.get(url, headers=headers)
    result = response.json()
    # result type은 dict . dict get 메서드이용해서 필드가 없을 경우 none 입력.
    if overview_is_valid(overview = result.get('overview')):
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
            genre = Genre.objects.get(pk=genredict.get('id'))

            movie.genres.add(genre)
        serializer = MovieSerializer(movie)
        # if serializer.is_valid(raise_exception=True):
            # serializer.save()
            
        return Response(serializer.data)
    else:
        return Response({'status':'fail'})

@api_view(['GET'])
def movie_detail_similar(request, movie_pk):
    
    url = "https://api.themoviedb.org/3/movie/"+ str(movie_pk) + "/recommendations?language=ko-KR&page=1"
    global headers

    response = requests.get(url, headers=headers)
    result = response.json()
    
    i = 0

    # while not overview_is_valid(result.get("results")[i].get("overview")):
    #     # out of range 에러 남 len(result.get("results")) 보다 작을 때 까지 조건 추가.
    #     i += 1
    result = result.get("results")[i]
    
    
    data = {
        'id' : result.get('id'),
        'poster_path' : result.get('poster_path'),
    }
    
    return Response(data)


@api_view(['POST'])
def movie_like(request, movie_pk):
    user = User.objects.get(pk = request.data.get('userID'))
    movie = get_object_or_404(Movie, pk=movie_pk)
    if user in movie.like_users.all():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def movie_today(request, movie_pk):
    user = User.objects.get(pk=request.data.get('userID'))
    movie = Movie.objects.get(pk=movie_pk)

    if user.today_movie == movie:
        user.today_movie = None  
        # movie와 동일한 경우 today_movie를 null로 설정
    else:
        user.today_movie = movie  
        # movie와 다른 경우 today_movie를 해당 movie로 설정

    user.save()  # 변경사항 저장
    serializer = UserSerializer(user)
    return Response(serializer.data)

