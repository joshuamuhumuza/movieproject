from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from firstApp.models import *


class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('previlages',)