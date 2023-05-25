from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer
from movies.models import Movie
from accounts.models import User
from accounts.serializers import UserInteractionSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def total_review_list(request):
    reviews = Review.objects.order_by("-created_at")
    serializer = ReviewSerializer(reviews, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    reviews = movie.reviews.all()
    serializer = ReviewSerializer(reviews,many= True)
    return Response(serializer.data)

@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)

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
    user.level = 1 + user.total_point // 100
    user.save()

    serializer = ReviewSerializer(review)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def review_detail(request, movie_pk, review_pk):
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

@api_view(['POST'])
def review_like(request, movie_pk, review_pk):
    user = User.objects.get(pk=request.data.get('userID'))
    review = get_object_or_404(Review, pk = review_pk)
    if user in review.like_users.all():
        review.like_users.remove(user)
    else:
        review.like_users.add(user)
        
    serializer = UserInteractionSerializer(user)
    return Response({'userInteractions': serializer.data})

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

    user = User.objects.get(pk = request.data.get('userID'))
    
    comment.user = user
    comment.review = review

    user.total_point += 2
    user.current_point += 2
    user.level = 1 + user.total_point // 100
    user.save()

    comment.save()
    serializer = CommentSerializer(comment)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def comment_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def comment_like(request, review_pk, comment_pk):
    user = User.objects.get(pk=request.data.get('userID'))
    comment = get_object_or_404(Comment, pk = comment_pk)
    if user in comment.like_users.all():
        comment.like_users.remove(user)
    else:
        comment.like_users.add(user)
    serializer = UserInteractionSerializer(user)
    return Response({'userInteractions': serializer.data})