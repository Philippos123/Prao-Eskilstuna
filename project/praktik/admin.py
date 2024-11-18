from django.contrib import admin

from .models import PraoAnnons

class PraoAnnonsAdmin(admin.ModelAdmin):
    list_display = ('rubrik', 'företag', 'publicerad_datum', 'användare')  # Anpassa fälten som ska visas
    search_fields = ('rubrik', 'företag')  # Sökfält i admin

admin.site.register(PraoAnnons, PraoAnnonsAdmin)
