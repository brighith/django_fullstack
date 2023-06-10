from django.shortcuts import render, redirect
from .models import Ninja, Dojo


def index(request):
    context = {
        "dojo_objects": Dojo.objects.all(),
    }
    return render(request, 'index.html', context)


def adding_d(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
    )
    return redirect('/')


def adding_n(request):
    Ninja.objects.create(
        first_name=request.POST['first'],
        last_name=request.POST['last'],
        dojo=Dojo.objects.get(id=request.POST['dojo']),
    )

    return redirect('/')


def deleteDojo(request):
    dell = Dojo.objects.get(id=request.POST['delete']).delete()

    return redirect('/')
