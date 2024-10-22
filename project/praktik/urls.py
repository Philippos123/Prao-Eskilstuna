from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('prao/', views.prao, name='prao'),
    path('accounts/', include('allauth.urls')),

]