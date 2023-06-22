from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt


def index(request):

    context = {
        'users': User.objects.all()
    }

    return render(request, 'index.html', context)


def register(request):

    password_from_form = request.POST['password']
    pw_hash = bcrypt.hashpw(password_from_form.encode(),
                            bcrypt.gensalt()).decode()
    print("this is the password", pw_hash)
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            birthday=request.POST['birthday'],
            email=request.POST['email'],
            password=pw_hash
        )
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            request.session['user_first_name'] = logged_user.first_name
            request.session['userid'] = logged_user.id
            request.session['status'] = "Registered"
        return redirect('/success')


def login(request):

    user = User.objects.filter(email=request.POST['email'])
    print(user)
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            request.session['user_first_name'] = logged_user.first_name
            request.session['status'] = "Logged in"
            return redirect('/success')
    return redirect("/")


def success(request):

    if "userid" not in request.session:
        print("this works")
        return redirect("/")
    return render(request, 'success.html')


def delete(request):

    del request.session['user_first_name']
    del request.session['user_id']

    return redirect('/')
