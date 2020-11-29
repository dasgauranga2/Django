from django.forms import ModelForm
from . models import Todo

# we want to create and save todo tasks
# a form is needed for the user to enter data
# here we create a custom form
class TodoForm(ModelForm):
    class Meta:
        # we have to specify the model for which the form is created
        model = Todo
        # we specify the fields of the model which we want the user to enetr
        fields = ['title','memo']