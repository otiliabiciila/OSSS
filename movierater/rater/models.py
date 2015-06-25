from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name
