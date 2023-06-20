from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.shows),
    path('shows/new/', views.add_new),
    path('submit_new/', views.submit_new),
    path('shows/<int:show_id>/', views.show_details),
    path('shows/<int:show_id>/edit', views.edit_page),
    path('edit/', views.edit_show),
    path('shows/<show_id>/delete/', views.delete),
]
