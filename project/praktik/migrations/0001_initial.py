# Generated by Django 4.2.16 on 2024-10-24 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PraoAnnons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('företag', models.CharField(max_length=255)),
                ('rubrik', models.CharField(max_length=255)),
                ('beskrivning', models.TextField()),
                ('kontaktperson', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.CharField(max_length=20)),
                ('publicerad_datum', models.DateTimeField(auto_now_add=True)),
                ('användare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
