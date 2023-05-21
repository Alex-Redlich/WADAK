from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('update/<int:user_pk>', views.update),
    path('delete/<int:user_pk>', views.delete),
]
