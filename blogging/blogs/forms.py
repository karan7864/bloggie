# forms.py
from django.forms import ModelForm
from django import forms
from .models import Comment, UserProfile


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [ 'text']


class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['fname', 'lname', 'password', 'email']
