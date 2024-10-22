from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('prao/', views.prao, name='prao'),
]