from django.shortcuts import render, redirect


def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1

    else:
        request.session['counter'] = 1

    return render(request, 'index.html')


def destroy(request):
    request.session['counter'] = 0

    return redirect("/")


def add_two(request):
    request.session['counter'] += 2

    return render(request, 'index.html')
