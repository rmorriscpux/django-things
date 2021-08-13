from django.db import models
import re
from datetime import date, timedelta

# Create your models here.
class Validations(models.Manager):
    def registration_validator(self, postData):
        # Initialize empty dictionary.
        errors = {}

        # Regular Expression Check
        NAME_REGEX = re.compile(r'^[a-zA-Z][a-zA-Z]+$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        # Check Inputs.
        if not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First Name must be at least 2 letters."
        
        if not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last Name must be at least 2 letters."

        try:
            entered_birthday = date.fromisoformat(postData['birthday'])
        except:
            errors['birthday'] = "Invalid birthday date."
        else:
            if entered_birthday > date.today().replace(year=date.today().year-13):
                errors['birthday'] = "Must be at least 13 years of age to register."

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address."
        else:
            find_email = self.filter(email=postData['email'])
            if find_email:
                errors['email'] = "Email address already registered."

        if len(postData['user_pw']) < 8:
            errors['user_pw'] = "Password must be at least 8 characters."
        elif postData['user_pw'] != postData['confirm_pw']:
            errors['user_pw'] = "Passwords do not match."
        
        return errors

class User(models.Model):
    # Unique Fields
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.CharField(max_length=255, unique=True)
    pw_hash = models.CharField(max_length=255)

    # Relationships

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Manager
    objects = Validations()