from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

# function for displaying the home page
def home(request):
    # returning the html file 
    return render(request, 'home.html')


# function for displaying the generated password page
def password(request):

    characters = list('abcdefghi123456')

    # get the user input from the html form
    gen_password = request.GET.get('input_password')
    gen_password = gen_password + "_"

    for _ in range(6):
        gen_password = gen_password + random.choice(characters)

    # returning the html file 
    # pass data to the html file using a dictionary
    return render(request, 'password.html', {'password':gen_password})
