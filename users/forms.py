from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'name', 'lastname', 'age', 'email', 'password']
