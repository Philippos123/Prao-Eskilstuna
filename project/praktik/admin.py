from django.contrib import admin

from .models import *

class PraoAnnonsAdmin(admin.ModelAdmin):
    list_display = ('rubrik', 'företag', 'publicerad_datum', 'användare')  # Anpassa fälten som ska visas
    search_fields = ('rubrik', 'företag')  # Sökfält i admin

admin.site.register(PraoAnnons, PraoAnnonsAdmin)

# admin.py
class NyhetAdmin(admin.ModelAdmin):
    list_display = ('titel', 'publicerad_datum')  # Använd 'titel' istället för 'title'
    search_fields = ('titel',)  # Använd 'titel' istället för 'title'
    list_filter = ('publicerad_datum',)

admin.site.register(Nyhet, NyhetAdmin)

