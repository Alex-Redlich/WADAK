from django.urls import path
from . import views

app_name = 'communities'
urlpatterns = [
    path('allreviews/',views.total_review_list),
    
    path('movie/<int:movie_pk>/review/',views.review_list),
    path('movie/<int:movie_pk>/review/create/',views.review_create),
    
    path('movie/<int:movie_pk>/review/<int:review_pk>/',views.review_detail),
    path('movie/<int:movie_pk>/review/<int:review_pk>/update/',views.review_update),
    path('movie/<int:movie_pk>/review/<int:review_pk>/delete/',views.review_delete),
    
    path('movie/<int:movie_pk>/review/<int:review_pk>/like/',views.review_like),
    
    path('review/<int:review_pk>/comment/',views.comment_list),
    path('review/<int:review_pk>/comment/create/',views.comment_create),
    
    path('review/<int:review_pk>/comment/<int:comment_pk>/update/',views.comment_update),
    path('review/<int:review_pk>/comment/<int:comment_pk>/delete/',views.comment_delete),
    
    path('review/<int:review_pk>/comment/<int:comment_pk>/like/',views.comment_like),
    
]
