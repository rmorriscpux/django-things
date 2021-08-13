from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from site_app.models import User

# wall
# Path: '/wall/'
# Main splash page for messages and comments.
def wall(request):
    if request.session.keys():
        this_user = User.objects.get(id=request.session['user_id'])
        context = {
            'all_messages' : Message.objects.all().order_by('-created_at'),
            'user_first_name' : this_user.first_name,
            'user_last_name' : this_user.last_name,
            'user_email' : this_user.email,
        }
        return render(request, 'wall.html', context)
    else:
        messages.error(request, "Please log in.")
        return redirect('/')

# add_msg
# Path: '/wall/add/'
# Add a message to the wall.
def add_msg(request):
    if request.session.keys():
        if request.method == "POST":
            # We need the author who made the message, and the actual message content.
            this_user = User.objects.get(id=request.session['user_id'])
            msg_content = request.POST['msg_content']
            # Add the new message to the database.
            if len(msg_content) > 0: # Ensure there is something in the message.
                new_msg = Message.objects.create(
                    content=msg_content,
                    author=this_user,
                )
                messages.success(request, "New message posted!")
            else:
                messages.error(request, "Error: Message cannot be blank.")
        
        return redirect('/wall/')
    else:
        messages.error(request, "Please log in.")
        return redirect('/')

# add_comment
# Path: '/wall/<int:msg_id>/comment/'
# Add a comment to a message.
def add_comment(request, msg_id):
    if request.session.keys():
        if request.method == "POST":
            # We need the author, the associated message, and the comment content.
            this_user = User.objects.get(id=request.session['user_id'])
            comment_content = request.POST['comment_content']
            # Add the new comment to the database.
            if len(comment_content) > 0:
                new_comment = Comment.objects.create(
                    content=comment_content,
                    message=Message.objects.get(id=msg_id),
                    author=this_user,
                )
                messages.success(request, "Comment added successfully!")
            else:
                messages.error(request, "Error: Comment cannot be blank.")

        return redirect('/wall/')
    else:
        messages.error(request, "Please log in.")
        return redirect('/')

