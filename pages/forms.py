from django import forms
from .models import ConcatUs



class ContacUsForm(forms.ModelForm):
    class Meta:
        model= ConcatUs
        fields = ('name', 'email', 'phone', 'body', )