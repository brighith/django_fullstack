from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
from datetime import datetime


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "bonus": datetime.now()
    }
    return render(request, 'index.html', context)
