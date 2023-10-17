from django import forms
from .models import Problem
from django.contrib.auth.models import User

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        exclude = ['user', 'status']
