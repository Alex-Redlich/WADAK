from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Review, Comment
from .serializers import ReviewListSerializer, ReviewSerializer,CommentSerializer
from ..movies.models import Movie

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['GET'])
def review_list(request, movie_pk):
    # 리뷰 리스트에서 내용을 보여줄건지
    movie = get_object_or_404(Movie, pk = movie_pk)
    reviews = movie.reviews.all()
    serializer = ReviewListSerializer(reviews,many= True)
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
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
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


@api_view(['GET'])
def comment_list(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    comments = review.comments.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
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
