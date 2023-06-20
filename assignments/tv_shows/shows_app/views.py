
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show
from datetime import datetime, date


def shows(request):
    context = {
        "shows": Show.objects.all(),
    }
    return render(request, 'shows.html', context)


def add_new(request):
    return render(request, 'new.html')


def submit_new(request):

    errors = Show.objects.basic_validator(request.POST)
    show_id = request.POST['show_id']

    # if Show.objects.filter(title=request.POST['title']).exists():
    #     messages.error(request, "this Title Exist, try to use a unique Title")
    #     return redirect('/shows/new')
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    else:
        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        return redirect('/shows/'+show_id)


def show_details(request, show_id):

    context = {
        'show_id': show_id,
        'show': Show.objects.get(id=show_id)
    }

    return render(request, 'show_details.html', context)


def edit_page(request, show_id):
    context = {
        'show_id': show_id,
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)


def edit_show(request):
    errors = Show.objects.basic_validator(request.POST)
    show_id = request.POST['show_id']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+show_id+'/edit')
    else:
        c = Show.objects.get(id=show_id)
        c.title = request.POST['title']
        c.network = request.POST['network']
        c.release_date = request.POST['release_date']
        c.description = request.POST['description']
        c.save()
    return redirect('/shows/'+show_id)


def delete(request, show_id):
    show_id = show_id
    d = Show.objects.get(id=show_id)
    d.delete()
    return redirect('/shows')
