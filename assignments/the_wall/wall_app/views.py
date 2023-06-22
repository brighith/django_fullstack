from django.shortcuts import render, redirect
from log_reg_app.models import User
from wall_app.models import Message, Comment


def wall(request):
    context = {
        "users": User.objects.all(),
        "messages": Message.objects.all(),
        "comments": Comment.objects.all()
    }
    return render(request, 'wall.html', context)
