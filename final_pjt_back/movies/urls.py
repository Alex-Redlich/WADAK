from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('getgenres/', views.get_genres),
    # 장르 받아오는거.
    path('<int:movie_pk>/', views.movie_detail),
    path('recent/',views.movie_recent),
    path('popular/',views.movie_popular),
    path('ranker/',views.movie_ranker),
    # path('pick/influncer/',),
    path('friend/<int:user_pk>/like/',views.movie_friend_like),
    path('friend/<int:user_pk>/today/',views.movie_friend_today),
    path('friend/<int:user_pk>/review/',views.movie_friend_review),
]
