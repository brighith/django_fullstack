from django.shortcuts import render, redirect
from .models import user

# Create your views here.


def index(request):
    context = {
        "Users": user.objects.all()
    }

    return render(request, "index.html", context)


def process(request):
    user.objects.create(first_name=request.POST['first'], last_name=request.POST['last'],
                        email_address=request.POST['email'], age=request.POST['age'])

    return redirect('/')
