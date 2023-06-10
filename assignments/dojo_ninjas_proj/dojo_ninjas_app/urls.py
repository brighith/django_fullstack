from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('adding_n', views.adding_n),
    path('adding_d', views.adding_d),
    path('deleteDojo', views.deleteDojo)

]
