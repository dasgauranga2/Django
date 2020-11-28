from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()
