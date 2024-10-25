from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PraoAnnonsForm
from .models import PraoAnnons

def home(request):
    return render(request, 'home.html')

def prao(request):
    annonser = PraoAnnons.objects.all()  # Hämta alla annonser

    # Filtrering
    företag_filter = request.GET.get('företag', '')
    rubrik_filter = request.GET.get('rubrik', '')

    if företag_filter:
        annonser = annonser.filter(företag__icontains=företag_filter)

    if rubrik_filter:
        annonser = annonser.filter(rubrik__icontains=rubrik_filter)

    return render(request, 'prao-base.html', {'annonser': annonser})

def login(request):
    return render(request, 'allauth/login.html')

def signup(request):
    return render(request, 'allauth/signup.html')

@login_required
def skapa_annons(request):
    if request.method == "POST":
        form = PraoAnnonsForm(request.POST, request.FILES)
        if form.is_valid():
            annons = form.save(commit=False)
            annons.användare = request.user  # Koppla annonsen till det inloggade företaget
            annons.save()
            return redirect('prao')  # Omdirigera till listan över annonser efter skapande
    else:
        form = PraoAnnonsForm()
    return render(request, 'annonser/skapa_annons.html', {'form': form})


def annons_detajl(request, annons_id):
    annons = get_object_or_404(PraoAnnons, id=annons_id)
    return render(request, 'annonser/annons_detajl.html', {'annons': annons})