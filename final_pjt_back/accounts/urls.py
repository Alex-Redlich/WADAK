from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('profile/<int:user_pk>/', views.profile_detail),
    path('profile/<int:user_pk>/follow/', views.follow),
    path('profile/<int:user_pk>/review/', views.review_list),
    path('profile/<int:user_pk>/like/', views.like_list),
    
    path('chinghopick/',views.chingho_pick),

    path('signup/', views.signup),
    path('login/', views.login),
    
    path('update/<int:user_pk>', views.update),
    path('delete/<int:user_pk>', views.delete),
]
