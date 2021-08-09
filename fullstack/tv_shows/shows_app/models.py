from django.db import models
from datetime import date

class TVShowValidations(models.Manager):
    # Validate form input
    def form_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters."

        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters."

        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['description'] = "Description must be at least 10 characters."
        
        try:
            release_date = date.fromisoformat(postData['release_date'])
        except:
            errors['release_date'] = "Invalid Date Format."
        else:
            if release_date > date.today():
                errors['release_date'] = "Release Date must be in the past."
        finally:
            return errors

    # Check for unique title when adding or editing a show. Exclude the show itself when editing.
    def unique_title(self, show_title, show_id=0):
        show_query = self.exclude(id=show_id).filter(title=show_title) # SELECT * FROM TVShows WHERE NOT id=show_id AND title=show_title;
        
        if len(show_query) > 0: # Found a show with the same title.
            return True
        else:
            return False


class TVShow(models.Model):
    # Unique Fields
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationships

    # Display Methods
    def get_release_date(self):
        return self.release_date.strftime("%B %d, %Y")

    # Manager
    objects = TVShowValidations()