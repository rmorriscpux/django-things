from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# index
# Path: '/'
# Display form to add new course, and the list of courses.
def index(request):
    context = {
        'all_courses' : Course.objects.all(),
    }
    return render(request, "index.html", context)

# add_course
# Path: '/add_course/'
# Add new course and redirect to the root page.
def add_course(request):
    if request.method == "POST":
        # Check form data.
        errors = Course.objects.form_validator(request.POST)
        
        if len(errors) > 0: # Errors found. Add messages and return.
            for key, value in errors.items():
                messages.error(request, value)

        else: # No errors. Add new course.
            new_course = Course.objects.create(
                name = request.POST['course_name'],
            )
            Description.objects.create(
                content = request.POST['course_description'],
                course = new_course,
            )
            messages.success(request, f"Course '{new_course.name}' Created!")
    
    return redirect('/')

# confirm_page
# Path: '/destroy/<int:course_id>/'
# Display confirmation page to destroy course.
def confirm_page(request, course_id):
    context = {
        'selected_course' : Course.objects.get(id=course_id),
    }
    return render(request, "destroy_confirm.html", context)

# destroy
# Path: '/destroy/<int:course_id>/confirm/'
# Deletes selected course.
def destroy(request, course_id):
    if request.method == "POST":
        try:
            to_delete = Course.objects.get(id=course_id)
        except:
            messages.error(request, f"Course ID {course_id} not found.")
        else:
            messages.success(request, f"Course '{to_delete.name}' removed successfully.")
            to_delete.delete()
        
    return redirect('/')

# course_info
# Path: '/info/<int:course_id>/'
# Goes to page for info and comments for selected course.
def course_info(request, course_id):
    try:
        get_course = Course.objects.get(id=course_id)
    except:
        messages.error(request, f"Course ID {course_id} not found.")
        return redirect('/')
    else:
        context = {
            'selected_course' : get_course
        }
        return render(request, "course_desc.html", context)

# add_comment
# Path: '/info/<int:course_id>/comment/'
# Adds comment for selected course..
def add_comment(request, course_id):
    try:
        get_course = Course.objects.get(id=course_id)
    except:
        messages.error(request, f"Course ID {course_id} not found.")
        return redirect('/')
    else:
        if request.method == "POST":
            errors = Comment.objects.form_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)

            else: # No errors, add new comment.
                Comment.objects.create(
                    content = request.POST['comment'],
                    course = get_course
                )
                messages.success(request, "Comment added successfully.")

        return redirect(f'/info/{course_id}/')