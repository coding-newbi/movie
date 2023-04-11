from django import forms
from .models import Film


class filmform(forms.ModelForm):
    class Meta:
        model=Film
        fields=['name','genre','year','img']