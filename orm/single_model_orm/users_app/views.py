from django.shortcuts import render, redirect
from .models import User # Object relating to user table in database.

# Main "Display All Users" page.
def index(request):
    context = {
        'all_users' : User.objects.all()
    }
    return render(request, 'index.html', context)

# Add User Logic
def add_user(request):
    request.session['form_msg'] = ""
    if request.method == "POST":
        if (request.POST['first_name'] == "" or 
        request.POST['last_name'] == "" or
        request.POST['email_address'] == "" or
        request.POST['age'] == ""):
            request.session['form_msg'] = "Missing Required Field(s)!"
        else:
            User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email_address = request.POST['email_address'],
                age = request.POST['age'],
            )
            request.session['form_msg'] = "New User Created!"
    return redirect('/')