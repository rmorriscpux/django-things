from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def result(request):
    return render(request, "result.html")

def set_data(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comments']
    request.session['fave_food'] = request.POST['fave_food']
    request.session['clothing'] = request.POST.getlist('clothing')

    return redirect('/result')

def reset_all(request):
    request.session.flush()
    return redirect('/')