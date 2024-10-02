from django.shortcuts import render, redirect
from .models import Azienda1, Sede1, Dipendente1
from django.shortcuts import get_object_or_404
from .forms import DipendenteForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def lista_dipendenti(request):
    aziende = Azienda1.objects.all()
    dipendenti = Dipendente1.objects.all()
    sedi = Sede1.objects.all()
    return render(request, 'lista_dipendenti.html', {'aziende':aziende, 'dipendenti':dipendenti, 'sedi':sedi})

def dipendente_azienda(request, azienda_slug):
    azienda = get_object_or_404(Azienda1, slug=azienda_slug)
    aziende = Azienda1.objects.all()
    dipendenti = Dipendente1.objects.filter(azienda=azienda)
    return render(request, 'dipendente_azienda.html', {'azienda' : azienda, 'dipendenti' : dipendenti, 'aziende' : aziende})


def dipendente_sede(request, sede_slug):
    sede = get_object_or_404(Sede1, slug=sede_slug)
    sedi = Sede1.objects.all()
    dipendenti = Dipendente1.objects.filter(sede=sede)
    return render(request, 'dipendente_sede.html', {'sede' : sede, 'sedi' : sedi, 'dipendenti' : dipendenti} )



def dipendente_detail(request, dipendente_nome):
    dipendente = get_object_or_404(Dipendente1, nome=dipendente_nome)
    return render(request, 'dipendente_detail.html', {'dipendente' : dipendente})


def create_dipendente(request):
    form = DipendenteForm()
    
    if request.method == 'POST':
        form = DipendenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
            

    context={'form':form}
    return render(request, 'crud/form_dipendente.html', context)

def update_dipendente(request, nome):

    dipendente = Dipendente1.objects.get(nome=nome) 
    form = DipendenteForm(instance=dipendente)

    if request.method == 'POST':
        form = DipendenteForm(request.POST, request.FILES, instance=dipendente)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'crud/form_dipendente.html', context)

def delete_dipendente(request, pk):
    dipendente = Dipendente1.objects.get(id=pk)
    if request.method == 'POST':
        dipendente.delete() #cancello il dipendente che ho preso con l'id

   
    context = {'dipendente' : dipendente}
    return render(request, 'crud/delete_dipendente.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('managementApp:login')
    
    else:
        form = UserCreationForm()

   
    context = { 'form' : form}
    return render(request, 'registration/register.html',context)

def login(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return redirect('managementApp:lista_dipendenti')
    
    else: 
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form' : form})
    
