from django.db import models

# Create your models here.
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title
