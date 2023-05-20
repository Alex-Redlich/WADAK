from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('getgenres/', views.get_genres),
    # 장르 받아옴
    path('recent/',views.get_movie_recent),
    path('popular/',views.get_movie_popular),
    path('<int:movie_pk>/', views.movie_detail),
    path('search/<str:keyword>/', views.movie_search),

    path('ranker/',views.movie_ranker),
    # path('pick/influncer/',),
    path('friend/<int:user_pk>/like/',views.movie_friend_like),
    path('friend/<int:user_pk>/today/',views.movie_friend_today),
    path('friend/<int:user_pk>/review/',views.movie_friend_review),
]
