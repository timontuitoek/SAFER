from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

# form for creating new user
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'receive_alerts']
        widgets = {
            'receive_alerts': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }