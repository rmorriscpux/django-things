from django.shortcuts import render, redirect
from .models import *
import datetime

# new_show_form: 
# Path: /shows/new
# Template: New_Show.html
# Display template to add a new TV show. No context needed.
def new_show_form(request):
    return render(request, 'New_Show.html')

# add_new_show: 
# Path: /shows/create/
# Redirect Path: /shows/<int:show_id>
# Logic for adding a new TV show to the database.
def add_new_show(request):
    if request.method == "POST":
        if (
            request.POST['title'] == "" or
            request.POST['network'] == "" or
            request.POST['release_date'] == ""
        ):
            request.session['form_msg'] = "Create Show: Fields Missing."
            return redirect('/shows/new/')
        else:
            new_show = TVShow.objects.create(
                title = request.POST['title'],
                network = request.POST['network'],
                release_date = request.POST['release_date'],
                description = request.POST['description'],
            )
            request.session['form_msg'] = "New Show Created."
            return redirect('/shows/' + str(new_show.id) + '/')
    else:
        request.session['form_msg'] = ""
        return redirect('/shows/new/')

# display_show
# Path: /shows/<int:show_id>/
# Template: TV_Show.html
# Display the details of a selected show ID.
# If show ID does not exist, go to /shows/.
def display_show(request, show_id):
    try:
        requested_show = TVShow.objects.get(id=show_id)
    except:
        return redirect('/shows/')
    else:
        context = {
            'tv_show' : requested_show,
        }
        return render(request, 'TV_Show.html', context)

# shows_list
# Path: /shows/
# Template: Shows_List.html
# Display a list of shows with Edit, Delete, Add options.
def shows_list(request):
    context = {
        'all_shows' : TVShow.objects.all(),
    }
    return render(request, 'Shows_List.html', context)

# edit_show_form
# Path: /shows/<int:show_id>/edit/
# Template: Edit_Show.html
# Display template to edit a TV show.
def edit_show_form(request, show_id):
    try:
        requested_show = TVShow.objects.get(id=show_id)
    except:
        return redirect('/shows/')
    else:
        context = {
            'tv_show' : requested_show,
        }
        return render(request, 'Edit_Show.html', context)

# update_show
# Path: /shows/<int:show_id>/update/
# Redirect to /shows/<int:show_id>/
def update_show(request, show_id):
    if request.method == "POST":
        if (
            request.POST['title'] == "" or
            request.POST['network'] == "" or
            request.POST['release_date'] == ""
        ):
            request.session['form_msg'] = "Edit Show: Fields Missing."
            return redirect('/shows/' + str(show_id) + '/')
        else:
            show_to_update = TVShow.objects.get(id=show_id)
            show_to_update.title = request.POST['title']
            show_to_update.network = request.POST['network']
            show_to_update.release_date = request.POST['release_date']
            show_to_update.description = request.POST['description']
            show_to_update.save()
            request.session['form_msg'] = "Show Updated."
            return redirect('/shows/' + str(show_id) + '/')
    else:
        request.session['form_msg'] = ""
        return redirect('/shows/' + str(show_id) + '/edit/')

# destroy_show
# Path: /shows/<int:show_id>/destroy/
# Redirect to /shows/
# Deletes a show from the list.
def destroy_show(request, show_id):
    if request.method == "POST":
        try:
            show_to_delete = TVShow.objects.get(id=show_id)
        except:
            request.session['form_msg'] = "Show Not Found."
        else:
            show_to_delete.delete()
            request.session['form_msg'] = "Show " + str(show_id) + " Deleted."
        finally:
            return redirect('/shows/')
    return redirect('/shows/')

# index
# Path: /
# Redirect to /shows/
def index(request):
    return redirect('/shows/')