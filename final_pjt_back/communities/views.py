from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer
from movies.models import Movie
from accounts.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

@api_view(['GET'])
def total_review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    serializer = ReviewSerializer(reviews,many = True)
    return Response(serializer.data)


# Create your views here.
@api_view(['GET'])
def review_list(request, movie_pk):
    # 리뷰 리스트에서 내용을 보여줄건지
    movie = get_object_or_404(Movie, pk = movie_pk)
    reviews = movie.reviews.all()
    serializer = ReviewSerializer(reviews,many= True)
    return Response(serializer.data)
    
    # elif request.method == 'POST':
    #     serializer = ReviewSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    # #리뷰 생성
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    # user = get_object_or_404(User, pk=1)
    user = get_object_or_404(User, pk= request.data.get('userID'))

    review = Review()
    review.title = request.data.get('title')
    review.content = request.data.get('content')
    review.rating = request.data.get('rating')
    review.user = user
    review.movie = movie
    review.save()

    user.total_point += 5
    user.current_point += 5
    user.save()

    serializer = ReviewSerializer(review)
    # if serializer.is_valid(data=serializer.data):
    #     serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def review_detail(request, movie_pk, review_pk):
    # movie = get_object_or_404(Movie, pk = movie_pk)
    review = get_object_or_404(Review, pk = review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['PUT'])
def review_update(request, movie_pk, review_pk):
    review =  get_object_or_404(Review, pk = review_pk)
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','DELETE'])
def review_like(request, movie_pk, review_pk):
    # user = User.objects.get(pk=2)
    # user = request.user
    # 이렇게 구하는게 맞나..?
    user = User.objects.get(pk=request.data.get('userID'))
    review = get_object_or_404(Review, pk = review_pk)
    if user in review.like_users.all():
        review.like_users.remove(user)
    else:
        review.like_users.add(user)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)



@api_view(['GET'])
def comment_list(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    comments = review.comments.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    comment = Comment()
    comment.content = request.data.get('content')
    # comment.user = User.objects.get(pk = 1)

    user = User.objects.get(pk = request.data.get('userID'))
    
    comment.user = user
    comment.review = review

    user.total_point += 5
    user.current_point += 5
    user.save()

    comment.save()
    serializer = CommentSerializer(comment)
    # serializer = CommentSerializer(data=request.data)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save(review=review)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def comment_update(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def comment_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','DELETE'])
def comment_like(request, review_pk, comment_pk):
    # user = User.objects.get(pk=2)
    # user = request.user
    # 이렇게 구하는게 맞나..?
    user = User.objects.get(pk=request.data.get('userID'))
    comment = get_object_or_404(Comment, pk = comment_pk)
    if user in comment.like_users.all():
        comment.like_users.remove(user)
    else:
        comment.like_users.add(user)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)