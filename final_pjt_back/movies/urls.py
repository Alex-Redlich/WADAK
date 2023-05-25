from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('<int:movie_pk>/', views.movie_detail),
    path('search/<str:keyword>/', views.movie_search),
    path('<int:movie_pk>/like/', views.movie_like), 
    path('<int:movie_pk>/similar/',views.movie_detail_similar),
    path('<int:movie_pk>/today/',views.movie_today),

    path('recent/',views.recent_movie),
    path('popular/',views.popular_movie),
    path('ranker/',views.ranker_today_movie),
    path('<int:userID>/follow/like/',views.follow_like_movie),
    path('<int:userID>/follow/today/',views.follow_today_movie),
    path('<int:userID>/follow/review/',views.follow_review_movie),
]
