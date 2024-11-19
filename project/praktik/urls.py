from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='index'),
    path('prao/', views.prao, name='prao'),
    path('accounts/', include('allauth.urls')),
    path('skapa/', views.skapa_annons, name='skapa_annons'),
    path('<int:annons_id>/', views.annons_detajl, name='annons_detajl'),  # Detaljvy för annons
    
    # Lägg till URL för att visa användarens annonser
    path('mina_annonser/', views.mina_annonser, name='mina_annonser'),  # Lista användarens egna annonser
    
    # Lägg till URL för att redigera en specifik annons
    path('<int:annons_id>/edit/', views.edit_annons, name='edit_annons'),  # Redigera annons
    
    # Lägg till URL för att radera en specifik annons
    path('<int:annons_id>/radera/', views.radera_annons, name='radera_annons'),  # Radera annons
]

# Hantera mediafiler i utvecklingsläge
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)