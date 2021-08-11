from django.db import models

class FormManager(models.Manager):
    def form_validator(self, postData):
        errors = {}

        for key in postData.keys():
            if key == 'course_name':
                if len(postData[key]) < 5:
                    errors['course_name'] = "Course Name must be at least 5 characters."
            elif key == 'course_description':
                if len(postData[key]) < 15:
                    errors['course_description'] = "Course Description must be at least 15 characters."
            elif key == 'course_comment':
                if len(postData[key]) < 1:
                    errors['course_comment'] = "Comment cannot be empty."

        return errors

class Course(models.Model):
    # Unique Fields
    name = models.CharField(max_length=255)

    # Relationships

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Manager
    objects = FormManager()

class Description(models.Model):
    # Unique Fields
    content = models.TextField()

    # Relationships
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # Unique Fields
    content = models.TextField()

    # Relationships
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Manager
    objects = FormManager()