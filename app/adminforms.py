
"""
Definition of forms.
"""

#from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _


from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Sala, OpiekunSali, Rezerwacja, RezerwacjaStanowiska, RodzajSali, Rola, Stanowisko, Uzytkownik,SalaOpiekun
from django import forms



class RolaUpdate (forms.ModelForm):
     class Meta:
         model=Uzytkownik
         fields=('id_roli', )

class PrzydzialCreate (forms.ModelForm):
     class Meta:
         model=SalaOpiekun
         fields=('id_sali','id_opiekuna_sali', )

class OpiekunCreate (forms.ModelForm):
     class Meta:
         model=OpiekunSali
         fields=('imie','nazwisko','email', 'numer_telefonu', )
         
class Sala_Create (forms.ModelForm):
     class Meta:
         model=Sala
         fields=('nazwa_sali','budynek','opis_sali', 'id_rodzaju_sali', )

class Stanowisko_Create (forms.ModelForm):
     class Meta:
         model=Stanowisko
         fields=('nazwa_stanowiska','opis_stanowiska','stopien_zaawansowania', 'czy_dostepne','id_sali', )
