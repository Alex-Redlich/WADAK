from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import User

from communities.serializers import ReviewListSerializer, CommentSerializer
from movies.serializers import MovieSerializer

from .serializers import UserSerializer
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
    return Response({'status':'success', 'userID': user.pk})


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data.get('username'))
    if user.check_password(request.data.get('password')):
        return Response({'status':'success', 'userID': user.pk})
    else:
        return Response({'status':'fail'})

def logout(request):
    pass

@api_view(['PUT'])
def update(request, user_pk):
    # 유저 DB 업데이트
    user = get_object_or_404(User, pk = user_pk)
    user.username = request.data.get('username')
    user.password = request.data.get('password')
    user.nickname = request.data.get('nickname')
    user.intro = request.data.get('intro')
    user.is_public = request.data.get('is_public')
    user.save()
    
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, user_pk):
    # 유저 DB 삭제
    user = get_object_or_404(User, pk = user_pk)
    user.delete()
    return Response({'status':'deleted'})

@api_view(['GET'])
def profile_detail(request, user_pk):
    # 프로필 조회.. 유저 DB 조회나 다름없는듯?
    pass

@api_view(['PUT'])
def profile_update(request, user_pk):
    # 프로필 수정
    pass

# @api_view(['GET'])
# def chingho_list(request, user_pk):
#     user = get_object_or_404(User, pk = user_pk)
#     chingho = user.have_chinghos.all()
#     serializer = ChinghoSerializer(chingho, many=True)
    
#     return Response(serializer.data)

@api_view(['POST'])
def chingho_pick(request):
    user = get_object_or_404(User, pk = request.data.get("userID"))
    first = [
        "고독한", "내일이 없는", "멋쟁이", "거친 파도 속", "멸종 위기종", "신출귀몰", "낙원의", "100%", "유기농", "야망 있는", "가성비", "욕심 많은", "오프라인", "어설픈", "용의주도한", "초식", "아시아"
    ]
    second = ["무법자", "고어매니아", "빌런", "범생이", "살림꾼", "유저", "스나이퍼", "기술자", "속도광", "싸피생", "지식인", "젊은이", "강태공", "한량", "와닥죽돌이", "아티스트", "프린스"]
    user.chingho = random.choice(first) +" " + random.choice(second)
    
    return Response({'chingho' : user.chingho})
    # for selected in user.have_chinghos.filter(is_selected = True):
    # 이렇게 하는게 맞나... 중개테이블을 돌면서 is_selected 된거를 False로 바꿔줌
    # chingho_first = get_object_or_404(Chingho, pk = chingho_first)
    # chingho_second = get_object_or_404(Chingho, pk = chingho_second)
    # user - chingho first & second 간 중개테이블의 is_selected를 True 바꿔줌

    # request 안에 chingho_first, chingho_second 받아와야함
    pass

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
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request, user_pk):
    # 유저가 남긴 리뷰 리스트 반환
    user = get_object_or_404(User, pk = user_pk)
    reviews = user.reviews.all()
    serializer = ReviewListSerializer(reviews, many = True)
    
    return Response(serializer.data)

@api_view(['GET'])
def like_list(request, user_pk):
    # request 안에 review, movie, comment를 담아서 요청하기 => 각각 좋아요한 리뷰, 영화, 댓글 리스트 반환
    user = get_object_or_404(User, pk = user_pk)
    if request.data.get('required_data') == 'review':
        like_reviews = user.like_reviews.all()
        serailizer = ReviewListSerializer(like_reviews, many= True)
        # 좋아요한 리뷰
    elif request.data.get('required_data') == 'movie':
        like_movies = user.like_movies.all()
        serailizer = MovieSerializer(like_movies, many= True)
        # 좋아요한 영화
    else:
        like_comments = user.like_comments.all()
        serailizer = CommentSerializer(like_comments,many= True)
        # 좋아요한 댓글
    return Response(serailizer.data)

def rank_renewal():
    rankers = User.objects.filter(rank__gt=0)
    for ranker in rankers:
        ranker.rank = 0
        
    newrankers = User.objects.order_by('-total_point')[:5]
    i = 1
    for newranker in newrankers:
        newranker.rank = i
        i += 1
    