from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import PraoAnnons
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class PraoAnnonsForm(forms.ModelForm):
    class Meta:
        model = PraoAnnons
        fields = ['företag', 'rubrik', 'beskrivning','org_nummer', 'kontaktperson', 'email', 'telefon', 'adress', 'bild', 'annons_typ', 'bransch_typ']  # Lägg till annons_typ
        widgets = {
            'företag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ange företagsnamn'}),
            'rubrik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ange annonsrubrik'}),
            'beskrivning': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Beskriv prao-möjligheten', 'rows': 4}),
            'org_nummer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ange organisationsnummer'}),
            'kontaktperson': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ange kontaktperson'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'kontakt@foretag.se'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ange telefonnummer'}),
            'adress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ange företagsadress'}),
            'bild': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

