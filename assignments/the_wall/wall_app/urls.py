from django.urls import path
from . import views

urlpatterns = [
    path('wall/', views.wall),
    path('wall/message_post/', views.message_post),
    path('wall/message_comment/', views.message_comment),
    path('wall/message_delete/', views.message_delete),
    path('wall/comment_delete/', views.comment_delete),
]
