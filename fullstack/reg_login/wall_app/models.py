from django.db import models
from site_app.models import User

class Message(models.Model):
    # Unique Fields
    content = models.TextField()

    # Relationships
    author = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # Unique Fields
    content = models.TextField()

    # Relationships
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)