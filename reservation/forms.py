from django import forms

from .models import RezervModel


class RezervForm(forms.ModelForm):
    class Meta:
        model = RezervModel
        fields = '__all__'
