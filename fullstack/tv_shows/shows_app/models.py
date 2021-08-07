from django.db import models

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