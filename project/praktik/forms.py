from django import forms
from .models import PraoAnnons

class PraoAnnonsForm(forms.ModelForm):
    class Meta:
        model = PraoAnnons
        fields = ['företag', 'rubrik', 'beskrivning', 'kontaktperson', 'email', 'telefon']
        widgets = {
            'beskrivning': forms.Textarea(attrs={'rows': 4}),
        }