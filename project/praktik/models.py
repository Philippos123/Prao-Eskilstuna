from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class PraoAnnons(models.Model):
    ANNONSTYP_CHOICES = [
        ('apl', 'APL'),
        ('praktik', 'Praktik'),
        ('prao', 'Prao'),
    ]

    företag = models.CharField(max_length=255)
    rubrik = models.CharField(max_length=255)
    beskrivning = models.TextField()
    kontaktperson = models.CharField(max_length=255)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    annons_typ = models.CharField(max_length=10, choices=ANNONSTYP_CHOICES)
    publicerad_datum = models.DateTimeField(auto_now_add=True)
    användare = models.ForeignKey(User, on_delete=models.CASCADE)
    bild = models.ImageField(upload_to='prao_annonsbilder/', blank=True, null=True)

    def __str__(self):
        return self.rubrik