# from django.shortcuts import render


# def index(request):
#     return render(request, "index.html")


# def result(request):
#     print(request.POST(
#     name = request.POST('name')
#     location = request.POST('location')
#     language = request.POST('language')
#     more = request.POST('more')
#     time = request.POST('time')
#     comment = request.POST('comment')
#     context = {
#         "name": name,
#         "location": location,
#         "language": language,
#         "more": more,
#         "time": time,
#         "comment": comment
#     }
#     return render(request, "result.html", context)
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def result(request):
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    more = request.POST['more']
    time = request.POST['time']
    comment = request.POST['comment']
    context = {
        "name": name,
        "location": location,
        "language": language,
        "more": more,
        "time": time,
        "comment": comment
    }
    return render(request, "result.html", context)
