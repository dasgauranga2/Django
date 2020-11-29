from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)
    # foreign key stores the relationship between 'User' model and 'Todo' model
    # it creates an one-to-many relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
