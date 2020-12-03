from accounts_app.models import CustomUser
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm,CustomUserChangeForm

# custom user model
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    # specify our custom forms
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # specify our custom user model
    model = CustomUser
    # model fields we want to display in the admin page
    list_display = ['username','email']

# regsiter the custom models and forms in the admin page
admin.site.register(CustomUser,CustomUserAdmin)
