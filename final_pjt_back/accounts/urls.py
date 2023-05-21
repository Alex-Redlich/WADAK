from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('profile/<int:user_pk>/', views.profile),
    path('profile/<int:user_pk>/follow/', views.follow),
    path('profile/<int:user_pk>/review/', views.review),
    path('profile/<int:user_pk>/like/', views.like),
    path('profile/<int:user_pk>/update/', views.profile_update),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('update/<int:user_pk>', views.update),
    path('delete/<int:user_pk>', views.delete),
]
