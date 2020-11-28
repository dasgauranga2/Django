from django.shortcuts import render
from .models import Project

def home(request):
    # read all the data from the database
    # we specify the model class(table) we want to read
    projects = Project.objects.all()

    return render(request, 'home.html', {'projects':projects})
