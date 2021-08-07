from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        # Pull this from a table maybe?
        'state_abbrevs': ['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE',
                          'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA',
                          'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND',
                          'NE', 'NH', 'NJ', 'NM', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI',
                          'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV',
                          'WY'],
        'all_dojos' : Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    request.session['form_msg'] = ""
    if request.method == "POST":
        if (request.POST['dojo_name'] == "" or
            request.POST['city'] == "" or
            request.POST['state'] == ""):
            request.session['form_msg'] = "Dojo: Missing Required Field(s)!"
        else:
            Dojo.objects.create(
                name = request.POST['dojo_name'],
                city = request.POST['city'],
                state = request.POST['state'],
                desc = "New Dojo" # Putting something here, not actually using.
            )
            request.session['form_msg'] = "New Dojo Created!"
    return redirect('/')

def add_ninja(request):
    request.session['form_msg'] = ""
    if request.method == "POST":
        if (request.POST['ninja_first_name'] == "" or
            request.POST['ninja_last_name'] == "" or
            request.POST['dojo_id'] == ""):
            request.session['form_msg'] = "Ninja: Missing Required Field(s)!"
        else:
            Ninja.objects.create(
                first_name = request.POST['ninja_first_name'],
                last_name = request.POST['ninja_last_name'],
                dojo_id = Dojo.objects.get(id=request.POST['dojo_id'])
            )
            request.session['form_msg'] = "New Ninja Created!"
    return redirect('/')

def delete_dojo(request, dojo_id):
    if request.method == "POST":
        dojo_to_delete = Dojo.objects.get(id=dojo_id)
        request.session['form_msg'] = "Dojo " + dojo_to_delete.name + " Deleted!"
        dojo_to_delete.delete()
    return redirect('/')
