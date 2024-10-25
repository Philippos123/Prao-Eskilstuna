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
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)