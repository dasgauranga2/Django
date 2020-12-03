from django.shortcuts import render
from django.views.generic import TemplateView

# class-based view for displaying the home page
class HomePage(TemplateView):
    # specify the name of the template to render
    template_name = 'home.html'
