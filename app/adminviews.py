from django.conf import settings
from django.conf.urls import url
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#import services
import requests
import json
from .models import Sala, OpiekunSali, Rezerwacja, RezerwacjaStanowiska, RodzajSali, Rola, Stanowisko, Uzytkownik, SalaOpiekun
from .forms import CreateUserForm, SalaCreate,  OpiekunSaliCreate, RezerwacjaCreate,\
    RezerwacjaStanowiskaCreate, RodzajSaliCreate, RolaCreate, StanowiskoCreate, UzytkownikCreate
from .adminforms import RolaUpdate, PrzydzialCreate, OpiekunCreate, Sala_Create, Stanowisko_Create
import hashlib
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
@cache_page(60 * 15)
@csrf_protect


def adminpage(request):
    return render(request, 'app/adminpage/adminpage.html')

def adminuzytkownicy_retrieve(request):
    users=Uzytkownik.objects.all()
    return render(request, 'app/adminpage/adminuzytkownicy.html', {'uzytkownicy':users})

def adminsale_retrieve(request):
    sale=Sala.objects.all()
    return render(request, 'app/adminpage/adminsale.html', {'sale':sale})

def adminstanowiska_retrieve(request):
    stanowiska=Stanowisko.objects.all()
    return render(request, 'app/adminpage/adminstanowiska.html', {'stanowiska':stanowiska})

def adminopiekunowie_retrieve(request):
    opiekunowie=OpiekunSali.objects.all()
    return render(request, 'app/adminpage/adminopiekunowie.html', {'opiekunowie':opiekunowie})

def adminrezerwacje_retrieve(request):
    rezerwacje=RezerwacjaStanowiska.objects.all()
    return render(request, 'app/adminpage/adminrezerwacje.html', {'rezerwacje':rezerwacje})

def zmienrole(request, user_id):
    user_id = int(user_id)
    try:
        user = Uzytkownik.objects.get(id_uzytkownika = user_id)
    except Uzytkownik.DoesNotExist:
        return redirect('adminuzytkownicy')
    form = RolaUpdate(request.POST or None, instance = user)
    if form.is_valid():
       form.save()
       return redirect('adminuzytkownicy')
    return render(request, 'app/adminpage/zmienrole.html', {'zmienrole':form})

def anulujrezerwacje(request, id_rez):
    id_rez = int(id_rez)
    try:
        rez = RezerwacjaStanowiska.objects.get(id_rezerwacji_stanowiska = id_rez)
    except RezerwacjaStanowiska.DoesNotExist:
        return redirect('adminrezerwacje')
    if rez.czy_anulowana==False: 
        rez.czy_anulowana=True
    else:
        rez.czy_anulowana=False
    rez.save()
    return HttpResponseRedirect( '/adminpage/adminrezerwacje/')

def zmienstatus(request, id_stan):
    id_stan = int(id_stan)
    try:
        stan = Stanowisko.objects.get(id_stanowiska = id_stan)
    except Stanowisko.DoesNotExist:
        return redirect('adminstanowiska')
    if stan.czy_dostepne==False:
        stan.czy_dostepne=True
        stan.save()
    else:
        stan.czy_dostepne=False
        stan.save()
    return HttpResponseRedirect( '/adminpage/adminstanowiska/')

def przydzialy(request):
    przydzialy=SalaOpiekun.objects.all()
    return render(request, 'app/adminpage/przydzialy.html', {'przydzialy':przydzialy})

def nowyprzydzial(request):
    form = PrzydzialCreate(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('przydzialy')
    return render(request, 'app/adminpage/nowyprzydzial.html', {'nowyprzydzial':form})

def przydzial_delete(request, id_przy):
    id_przy = int(id_przy)
    try:
        przydzial = SalaOpiekun.objects.get(id_sala_opiekun = id_przy)
    except SalaOpiekun.DoesNotExist:
        return redirect('przydzialy')
    przydzial.delete()
    return redirect('przydzialy')

def nowyopiekun(request):
    form = OpiekunCreate(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('adminopiekunowie')
    return render(request, 'app/adminpage/nowyopiekun.html', {'nowyopiekun':form})

def opiekun_delete(request, id_op):
    id_op = int(id_op)
    try:
        opiekun = OpiekunSali.objects.get(id_opiekuna = id_op)
    except OpiekunSali.DoesNotExist:
        return redirect('adminopiekunowie')
    opiekun.delete()
    return redirect('adminopiekunowie')

def opiekun_update(request, id_op):
    id_op = int(id_op)
    try:
        opiekun = OpiekunSali.objects.get(id_opiekuna = id_op)
    except OpiekunSali.DoesNotExist:
        return redirect('adminopiekunowie')
    opiekun_form = OpiekunCreate(request.POST or None, instance = opiekun)
    if opiekun_form.is_valid():
       opiekun_form.save()
       return redirect('adminopiekunowie')
    return render(request, 'app/adminpage/nowyopiekun.html', {'nowyopiekun':opiekun_form})

def nowasala(request):
    form = Sala_Create(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('adminsale')
    return render(request, 'app/adminpage/nowasala.html', {'nowasala':form})

def sala_delete(request, id_sal):
    id_sal = int(id_sal)
    try:
        sala = Sala.objects.get(id_sali = id_sal)
    except Sala.DoesNotExist:
        return redirect('adminsale')
    sala.delete()
    return redirect('adminsale')

def sala_update(request, id_sal):
    id_sal = int(id_sal)
    try:
        sala = Sala.objects.get(id_sali = id_sal)
    except Sala.DoesNotExist:
        return redirect('adminsale')
    sala_form = Sala_Create(request.POST or None, instance = sala)
    if sala_form.is_valid():
       sala_form.save()
       return redirect('adminsale')
    return render(request, 'app/adminpage/nowasala.html', {'nowasala':sala_form})

def nowestanowisko(request):
    form = Stanowisko_Create(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('adminstanowiska')
    return render(request, 'app/adminpage/nowestanowisko.html', {'nowestanowisko':form})

def stanowisko_delete(request, id_stan):
    id_stan = int(id_stan)
    try:
        stanowisko = Stanowisko.objects.get(id_stanowiska = id_stan)
    except Stanowisko.DoesNotExist:
        return redirect('adminstanowiska')
    stanowisko.delete()
    return redirect('adminstanowiska')

def stanowisko_update(request, id_stan):
    id_stan = int(id_stan)
    try:
        stanowisko = Stanowisko.objects.get(id_stanowiska = id_stan)
    except Stanowisko.DoesNotExist:
        return redirect('adminstanowiska')
    stanowisko_form = Stanowisko_Create(request.POST or None, instance = stanowisko)
    if stanowisko_form.is_valid():
       stanowisko_form.save()
       return redirect('adminstanowiska')
    return render(request, 'app/adminpage/nowestanowisko.html', {'nowestanowisko':stanowisko_form})