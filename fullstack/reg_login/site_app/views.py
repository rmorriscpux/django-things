from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from datetime import date
from .models import *

# index
# Path: '/'
# Registration and Login Page
def index(request):
    # print(request.session.keys())
    context = {
        'cur_date' : date.today().isoformat()
    }
    return render(request, 'index.html', context)

# registration
# Path: '/register/'
# Register a new user.
def registration(request):
    if request.method == "POST":
        # Validate data.
        errors = User.objects.registration_validator(request.POST)

        if errors: # List error messages and go to main page.
            for err_msg in errors.values():
                messages.error(request, err_msg)
            return redirect('/')
        else: # No errors, complete registration.
            new_user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                birthday = request.POST['birthday'],
                email = request.POST['email'],
                pw_hash = bcrypt.hashpw(request.POST['user_pw'].encode(), bcrypt.gensalt()).decode()
            )
            messages.success(request, "Registration successful!")
            return redirect('/success/')

    else:
        return redirect('/')

# login
# Path: '/login/'
# Login user
def login(request):
    if request.method == "POST":
        get_user = User.objects.filter(email=request.POST['email'])

        if not get_user: # Email not found. Throw error and return.
            messages.error(request, "Invalid credentials.")
            return redirect('/')

        if bcrypt.checkpw(request.POST['user_pw'].encode(), get_user[0].pw_hash.encode()):
            request.session['user_id'] = get_user[0].id
            messages.success(request, "Login successful!")
            return redirect('/success/')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('/')

    else:
        return redirect('/')

# success
# Path: '/success/'
# Successful login or registration.
def success(request):
    # print(request.session.keys())
    if request.session.keys():
        return render(request, 'success.html')
    else:
        return redirect('/')

# logout
# Path: '/logout/'
# Logs out.
def logout(request):
    if request.session.keys():
        request.session.clear()
        messages.success(request, "Logout successful!")

    return redirect('/')