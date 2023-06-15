from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_new_book', views.add_book),
    path('authors', views.authors),
    path('add_new_author', views.add_authors),
    path('books/<int:book_id>', views.view_book),
    path('add_author/<int:book_id>', views.add_author_book),
    path('authors/<int:author_id>', views.view_author),
    path('add_book/<int:author_id>', views.add_book_author)
]
