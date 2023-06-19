from django.shortcuts import render, redirect
import random


def generate(request):
    request.session['getRandom'] = random.randint(1, 100)
    return redirect('/index')


def index(request):
    print("my random number is:", request.session['getRandom'])
    return render(request, 'index.html')


def answer(request):
    guess_left = request.session.get('guess_left', 5)
    randomNum = request.session.get('getRandom')
    newnumber = int(request.POST['newnumber'])
    if newnumber > 100:
        request.session["comments"] = "The number you inserted is invalid"
        request.session["numbers"] = "Please, choose a number between 1 and 100!"
        return redirect('/index')
    print("user number", newnumber)

    while guess_left > 1 and newnumber == randomNum:
        request.session["comments"] = "You WON!"
        request.session["numbers"] = "Wannaa Play again?"
        del request.session['guess_left']
        return redirect('/index')

    while guess_left > 1 and newnumber != randomNum:
        request.session['guess_left'] = guess_left - 1
        if newnumber > randomNum:
            request.session["comments"] = "Wrong answer, you are too high"
            request.session["numbers"] = "please try again!"
            return redirect('/index')
        if newnumber < randomNum:
            request.session["comments"] = "Wrong answer, you are too low"
            request.session["numbers"] = "please try again!"
            return redirect('/index')

    while guess_left <= 1:
        request.session['guess_left'] = guess_left - 1
        request.session["comments"] = "You lost!"
        request.session["numbers"] = "Try another game?"
        return redirect('/index')


def reset(request):
    request.session["comments"] = "Go ahead"
    request.session["numbers"] = "whats your strategy?"
    request.session['guess_left'] = 5
    return redirect('/')
