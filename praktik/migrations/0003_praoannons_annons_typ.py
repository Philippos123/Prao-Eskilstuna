# Generated by Django 5.1.2 on 2024-11-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praktik', '0002_praoannons_bild'),
    ]

    operations = [
        migrations.AddField(
            model_name='praoannons',
            name='annons_typ',
            field=models.CharField(choices=[('apl', 'APL'), ('prao', 'Prao'), ('praktik', 'Praktik')], default='prao', max_length=20),
        ),
    ]
