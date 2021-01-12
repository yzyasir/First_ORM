from django.db import models

# Create your models here. A table in our database.
class Movie(models.Model):
    # Movie inherits from models.Model, gets an implicit id whenever you create a new model
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)