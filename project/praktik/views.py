from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # För att visa meddelanden
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
        
    if 'type' in request.GET:
        selected_types = request.GET.getlist('type')  # Hämta alla valda typer
        if selected_types:
            annonser = annonser.filter(annons_typ__in=selected_types)
    if 'bransch' in request.GET:
        selected_branches = request.GET.getlist('bransch')
        if selected_branches:
            annonser = annonser.filter(bransch_typ__in=selected_branches)

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

@login_required
def mina_annonser(request):
    annonser = PraoAnnons.objects.filter(användare=request.user)  # Filtrera annonser baserat på inloggad användare
    return render(request, 'annonser/mina_annonser.html', {'annonser': annonser})

@login_required
def edit_annons(request, annons_id):
    annons = get_object_or_404(PraoAnnons, id=annons_id, användare=request.user)  # Säkerställ att användaren äger annonsen

    if request.method == "POST":
        form = PraoAnnonsForm(request.POST, request.FILES, instance=annons)
        if form.is_valid():
            form.save()
            messages.success(request, "Annonsen har uppdaterats.")
            return redirect('mina_annonser')
    else:
        form = PraoAnnonsForm(instance=annons)

    return render(request, 'annonser/edit_annons.html', {'form': form, 'annons': annons})

@login_required
def radera_annons(request, annons_id):
    annons = get_object_or_404(PraoAnnons, id=annons_id, användare=request.user)

    if request.method == "POST":
        annons.delete()
        messages.success(request, "Annonsen har tagits bort.")
        return redirect('mina_annonser')

    return render(request, 'annonser/radera_annons.html', {'annons': annons})