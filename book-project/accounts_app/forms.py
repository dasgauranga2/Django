from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# custom form for creating users
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # we specify our custom model
        model = get_user_model()
        fields = ('email','username')

# custom form for editing users
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        # we specify our custom model
        model = get_user_model()
        fields = ('email','username')