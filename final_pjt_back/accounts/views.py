from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import User

from movies.models import Movie

from communities.serializers import ReviewSerializer,CommentSerializer
from movies.serializers import MovieSerializer

from .serializers import UserSerializer, UserInteractionSerializer
import random
# Create your views here.

@api_view(['POST'])
def signup(request):
    # 유저 DB 생성
    user = User()
    
    user.username = request.data.get('username')
    user.set_password(request.data.get('password'))
    user.nickname = request.data.get('nickname')
    user.intro = request.data.get('intro')
        # 유효성 검사하기
        # id 가 중복될경우.
        # 패스워드가 잘못됬을 경우
        # 어쩌구저쩌구
    user.save()
    serializer = UserInteractionSerializer(user)
    return Response({'status':'success', 'userID': user.pk, 'userInteraction': serializer.data})


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data.get('username'))
    if user.check_password(request.data.get('password')):
        serializer = UserInteractionSerializer(user)
        print(serializer.data)
        return Response({'status':'success', 'userID': user.pk, 'userInteractions' : serializer.data})
    else:
        return Response({'status':'fail'})

@api_view(['PUT'])
def update(request):
    # 유저 DB 업데이트 (닉네임, 자기소개)
    user = get_object_or_404(User, pk = request.data.get('userID'))
    user.nickname = request.data.get('nickname')
    user.intro = request.data.get('intro')
    user.save()
    
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request):
    # 유저 DB 삭제 
    user = get_object_or_404(User, pk = request.data.get('userID'))
    user.delete()
    return Response({'status':'success'})

@api_view(['GET'])
def profile_detail(request, user_pk):
    user = get_object_or_404(User, pk = user_pk)
    
    serializer = UserSerializer(user)
    data = {
        'reviews_count' : user.reviews.count(),
        'comments_count' : user.comments.count()
    }
    data.update(serializer.data)
    return Response(data)

@api_view(['POST'])
def chingho_pick(request):
    user = get_object_or_404(User, pk = request.data.get("userID"))
    if user.current_point > 20:
        first = [
            "고독한", "내일이 없는", "멋쟁이", "거친 파도 속", "멸종 위기종", "신출귀몰", "낙원의", "100%", "유기농", "야망 있는", "가성비", "욕심 많은", "오프라인", "어설픈", "용의주도한", "초식", "아시아"
        ]
        second = [
            "무법자", "고어매니아", "빌런", "범생이", "살림꾼", "유저", "스나이퍼", "기술자", "속도광", "싸피생", "지식인", "젊은이", "강태공", "한량", "와닥죽돌이", "아티스트", "프린스"
        ]
        user.chingho = random.choice(first) +" " + random.choice(second)
        user.current_point -= 20
        user.save()
        return Response({'status': 'success', 'chingho' : user.chingho})
    return Response({'status': 'fail'})


@api_view(['POST'])
def follow(request, user_pk):
    # 타겟 유저를 팔로우/ 언팔로우
    # user = get_object_or_404(User, pk = 1)
    user = get_object_or_404(User, pk = request.data.get('userID'))
    target_user = get_object_or_404(User, pk = user_pk)
    if target_user in user.followings.all():
        user.followings.remove(target_user)
    else:
        user.followings.add(target_user)
    serializer = UserInteractionSerializer(user)
    return Response({'userInteractions' : serializer.data})

@api_view(['GET'])
def review_list(request, user_pk):
    # 유저가 리뷰 남긴 영화 리스트 반환
    user = get_object_or_404(User, pk = user_pk)
    reviews = user.reviews.all().order_by('-created_at')[:10]
    movie_ids = list(set([review.movie.id for review in reviews]))
    movies = Movie.objects.filter(id__in=movie_ids)[:3]

    serializer = MovieSerializer(movies, many = True)
    
    return Response(serializer.data)

@api_view(['GET'])
def like_list(request, user_pk):
    # 유저가 좋아요한 영화 리스트 반환
    user = get_object_or_404(User, pk = user_pk)
    like_movies = user.like_movies.all()[:3]

    serializer = MovieSerializer(like_movies, many = True)

    return Response(serializer.data)

def rank_renewal():
    rankers = User.objects.filter(rank__gt=0)
    for ranker in rankers:
        ranker.rank = 0
        ranker.save()
        
    newrankers = User.objects.order_by('-total_point')[:5]
    i = 1
    for newranker in newrankers:
        newranker.rank = i
        i += 1
        newranker.save()
    
    serializer = UserSerializer(newrankers)
    return Response(serializer.data)