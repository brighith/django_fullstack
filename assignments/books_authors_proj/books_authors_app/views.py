from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'index.html', context)


def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'], description=request.POST['description'])
    return redirect('/')


def authors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)


def add_authors(request):
    if request.method == 'POST':
        Author.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], description=request.POST['description'])
    return redirect('/authors')


def view_book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'author_book': Book.objects.get(id=book_id).authors.all(),
        'all_authors': Author.objects.all()
    }
    return render(request, 'view_book.html', context)


# def view_author(request, author_id):
#     context = {
#         'author': Author.objects.get(id=author_id),
#         'book_author': Author.objects.get(id=author_id).books.all(),
#         'all_books': Book.objects.exclude(id__in=Author.objects.get(id=author_id).books.all())
#     }
#     return render(request, 'view_author.html', context)


def add_author_book(request, book_id):
    Book.objects.get(id=book_id).authors.add(
        Author.objects.get(id=request.POST['author']))
    return redirect(f'/books/{book_id}')


def view_author(request, author_id):
    context = {
        'author': Author.objects.get(id=author_id),
        'book_author': Author.objects.get(id=author_id).books.all(),
        'all_books': Book.objects.all()
    }
    return render(request, 'view_author.html', context)

# def view_author(request, author_id):
#     context = {
#         'author': Author.objects.get(id=author_id),
#         'book_author': Author.objects.get(id=author_id).books.all(),
#         'all_books': Book.objects.exclude(id__in=Author.objects.get(id=author_id).books.all())
#     }
#     return render(request, 'view_author.html', context)


def add_book_author(request, author_id):
    Author.objects.get(id=author_id).books.add(
        Book.objects.get(id=request.POST['book']))
    return redirect(f'/authors/{author_id}')
