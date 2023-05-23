from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('getgenres/', views.get_genres),
    # 장르 받아옴
    path('<int:movie_pk>/', views.movie_detail),
    path('search/<str:keyword>/', views.movie_search),
    path('<int:movie_pk>/like/', views.movie_like), 
    path('<int:movie_pk>/similar/',views.movie_detail_similar),
        
    path('recent/',views.recent_movie),
    path('popular/',views.popular_movie),
    path('ranker/',views.ranker_today_movie),
    path('follow/<int:user_pk>/like/',views.follow_like_movie),
    path('follow/<int:user_pk>/today/',views.follow_today_movie),
    path('follow/<int:user_pk>/review/',views.follow_review_movie),
    
    # path('pick/influncer/',),
    # path('test/', views.popular_movie),
]
