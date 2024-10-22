from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def prao(request):
    return render(request, 'prao-base.html')