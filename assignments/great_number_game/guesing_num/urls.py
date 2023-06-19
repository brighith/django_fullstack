from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate),
    path('index/', views.index),
    path('index/show/', views.answer),
    path('index/play_again/', views.reset),
]
