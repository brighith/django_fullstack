from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(default="old dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    books = models.ManyToManyField(Book, related_name="books_authors")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
