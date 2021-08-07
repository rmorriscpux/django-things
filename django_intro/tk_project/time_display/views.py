from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.
def display_time(request):
    contents = {
        'time': strftime("%Y-%m-%d %H:%M %p", gmtime()),
    }
    return render(request, 'display_time.html', contents)