from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

# class-based view for signup
class SignupPage(generic.CreateView):
    # custom form for user creation 
    form_class = CustomUserCreationForm
    # after submitting the signup form 
    # the user is redirected to the following url path
    success_url = reverse_lazy('home')
    # name of the template to be rendered
    template_name = 'registration/signup.html'
