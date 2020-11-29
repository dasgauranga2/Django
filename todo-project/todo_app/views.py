from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import TodoForm
from .models import Todo

def home(request):

    return render(request, 'home.html')

def user_signup(request):
    
    if request.method == 'GET':
        # when the user wants to fill the signup form

        # UserCreationForm provides a form that creates a user from the given username and password
        return render(request, 'user_signup.html', {'form' : UserCreationForm()})
    else:
        # when the user submits the signup form
        try:
            # creating an User object
            user = User.objects.create_user(request.POST['username'],
                                    password=request.POST['password1'])
            # saving the User object
            user.save()

            # login the user using the 'User' object
            login(request,user)

            # redirect to 'current_todo' url path
            return redirect('current_todo')

        except IntegrityError:
            # IntegrityError occurs when the user tries to save the 'User' object
            # if the username already exists in the database
            return render(request, 'user_signup.html', {'form' : UserCreationForm(), 'error' : 'Username already taken'})

def current_todo(request):

    # retrieve the 'Todo' objects from the database
    # retrive only those objects where the 'user' field matches with the current user 
    todos = Todo.objects.filter(user=request.user) 

    return render(request, 'current_todo.html', {'todos' : todos})

def user_logout(request):

    if request.method == 'POST':
        # logout the user
        logout(request)

        return redirect('home')

def user_login(request):

    if request.method == 'GET':
        # when the user wants to fill the login form

        # UserCreationForm provides a form that creates a user from the given username and password
        return render(request, 'user_login.html', {'form' : AuthenticationForm()})
    else:
        # when the user submits the login form

        # authenticate the user
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        
        # if no user is found with the above username and password
        if user is None:
            return render(request, 'user_login.html', {'form' : AuthenticationForm(), 'error' : 'Username and password did not match'})
        else:
            # login the user using the 'User' object
            login(request,user)

            # redirect to 'current_todo' url path
            return redirect('current_todo')
        
def create_todo(request):

    if request.method == 'GET':
        # we will pass a custom form 
        return render(request, 'create_todo.html', {'form' : TodoForm()})
    else:
        # when the user submits the custom form
        
        # retrieve the data submitted by the user
        form = TodoForm(request.POST)
        # create a new 'Todo' object from the data entered by the user
        new_todo = form.save(commit=False)
        # the 'user' field of the object is the current user entering the data
        new_todo.user = request.user
        # save the object to the database
        new_todo.save()

        return redirect('current_todo')