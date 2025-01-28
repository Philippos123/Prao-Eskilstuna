from django.db import models
import os
import logging
from django.contrib.auth.models import User
    

class PraoAnnons(models.Model):
    ANNONSTYP_CHOICES = [
        ('apl', 'APL'),
        ('praktik', 'Praktik'),
        ('prao', 'Prao'),
    ]
    BRANSCHTYP_CHOICES = [
        ('teknik', 'Teknik'),
        ('vård', 'Vård'),
        ('handel', 'Handel'),
        ('service', 'Service'),
        ('fordon', 'Fordon'),
        ('industri', 'Industri'),
    ]

    företag = models.CharField(max_length=255)
    rubrik = models.CharField(max_length=255)
    beskrivning = models.TextField()
    org_nummer = models.CharField(max_length=12, null=True, blank=True)
    kontaktperson = models.CharField(max_length=255)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    annons_typ = models.CharField(max_length=10, choices=ANNONSTYP_CHOICES)
    bransch_typ = models.CharField(max_length=10, choices=BRANSCHTYP_CHOICES, default='Okänd')
    publicerad_datum = models.DateTimeField(auto_now_add=True)
    adress = models.CharField(max_length=255, null=True, blank=True)
    användare = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rubrik
    
def news_image_path(instance, filename):
    ext = filename.split('.')[-1]  # Get the file extension
    filename = f"{instance.titel.replace(' ', '_')}_image.{ext}"

    logger = logging.getLogger(__name__)
    logger.info(f"Instance title: {instance.titel}")
    logger.info(f"Generated filename: {filename}")

    return os.path.join('news_images', filename)


# models.py
class Nyhet(models.Model):
    titel = models.CharField(max_length=200)  # Fältet heter 'titel', inte 'title'
    beskrivning = models.TextField()
    publicerad_datum = models.DateTimeField(auto_now_add=True)
    användare = models.ForeignKey(User, on_delete=models.CASCADE)
    bild = models.ImageField(upload_to=news_image_path)

    def __str__(self):
        return self.titel  # Använd 'titel' här också
