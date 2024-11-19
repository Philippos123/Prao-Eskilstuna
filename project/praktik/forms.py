from django import forms
from .models import PraoAnnons

class PraoAnnonsForm(forms.ModelForm):
    class Meta:
        model = PraoAnnons
        fields = ['företag', 'rubrik', 'beskrivning', 'kontaktperson', 'email', 'telefon', 'bild', 'annons_typ', 'bransch_typ']  # Lägg till annons_typ
        widgets = {
            'företag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ange företagsnamn'}),
            'rubrik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ange annonsrubrik'}),
            'beskrivning': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Beskriv prao-möjligheten', 'rows': 4}),
            'kontaktperson': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ange kontaktperson'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'kontakt@foretag.se'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ange telefonnummer'}),
            'bild': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }