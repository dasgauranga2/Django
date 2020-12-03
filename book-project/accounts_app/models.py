from django.db import models
from django.contrib.auth.models import AbstractUser

# custom model for users
# instead of using the default 'User' model provided by django
# we create our own model
class CustomUser(AbstractUser):
    pass
