from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('prao/', views.prao, name='prao'),
    path('accounts/', include('allauth.urls')),
    path('skapa/', views.skapa_annons, name='skapa_annons'),
    path('<int:annons_id>/', views.annons_detajl, name='annons_detajl'),  # Detaljvy för annons
]