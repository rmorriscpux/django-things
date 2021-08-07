from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    return render(request, 'index.html')

def generate_word(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0

    request.session['word'] = ""
    for i in range(0, 14):
        request.session['word'] += chr(random.randint(65, 90))

    request.session['attempts'] += 1

    return redirect('/random_word')

def reset(request):
    request.session['attempts'] = 0
    request.session['word'] = ""
    return redirect('/random_word')