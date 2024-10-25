from django.db import models
from django.contrib.auth.models import User

class PraoAnnons(models.Model):
    företag = models.CharField(max_length=255)
    rubrik = models.CharField(max_length=255)
    beskrivning = models.TextField()
    kontaktperson = models.CharField(max_length=255)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    publicerad_datum = models.DateTimeField(auto_now_add=True)
    användare = models.ForeignKey(User, on_delete=models.CASCADE)
    bild = models.ImageField(upload_to='prao_annonsbilder/', blank=True, null=True)  # Lägg till detta fält

    def __str__(self):
        return self.rubrik