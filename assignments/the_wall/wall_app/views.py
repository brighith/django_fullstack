from django.shortcuts import render, redirect
from log_reg_app.models import User
from wall_app.models import Message, Comment


def wall(request):

    if "userid" not in request.session:
        print("this works")
        return redirect("/")

    context = {
        'users': User.objects.all(),
        'messages': Message.objects.all(),
        'comments': Comment.objects.all()
    }

    return render(request, 'wall.html', context)


def message_post(request):

    Message.objects.create(
        user=User.objects.get(id=request.POST['user_id']),
        message_text=request.POST['message_post']
    )
    print("this works here")

    return redirect("/wall")


def message_comment(request):

    Comment.objects.create(
        user=User.objects.get(id=request.POST['user_id']),
        message=Message.objects.get(id=request.POST['message_id']),
        comment_text=request.POST['comment_post']
    )

    return redirect('/wall')


def message_delete(request):

    w = Comment.objects.get(id=request.POST['user_id'])
    w.delete()
    return redirect('/wall')


def comment_delete(request):
    print("this works here in the comments section")

    c = Message.objects.get(id=request.POST['user.id'])
    c.delete()

    return redirect('/wall')
