"""
Definition of forms.
"""

#from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _


from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Sala,SalaOpiekun, OpiekunSali, Rezerwacja, RezerwacjaStanowiska, RodzajSali, Rola, Stanowisko, Uzytkownik
from django import forms

#class BootstrapAuthenticationForm(AuthenticationForm):
#    """Authentication form which uses boostrap CSS."""
#    username = forms.CharField(max_length=254,
#                               widget=forms.TextInput({
#                                   'class': 'form-control',
#                                   'placeholder': 'User name'}))
#    password = forms.CharField(label=_("Password"),
#                               widget=forms.PasswordInput({
#                                   'class': 'form-control',
#                                   'placeholder':'Password'}))

class CreateUserForm(UserCreationForm):
	  class Meta:
	        model = User
	        fields = ['username', 'email', 'password1', 'password2']





class SalaCreate(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'


class RolaCreate(forms.ModelForm):
    class Meta:
        model = Rola
        fields = '__all__'

class StanowiskoCreate(forms.ModelForm):
    class Meta:
        model = Stanowisko
        fields = '__all__'

class RodzajSaliCreate(forms.ModelForm):

    class Meta:
        model = RodzajSali
        fields = '__all__'

class OpiekunSaliCreate(forms.ModelForm):

    class Meta:
        model = OpiekunSali
        fields = '__all__'


class UzytkownikCreate(forms.ModelForm):

    class Meta:
        model = Uzytkownik
        fields = '__all__'

class RezerwacjaCreate(forms.ModelForm):
    class Meta:
        model = Rezerwacja
        fields = '__all__'

class RezerwacjaStanowiskaCreate(forms.ModelForm):

    class Meta:
        model = RezerwacjaStanowiska
        fields = '__all__'

class SalaOpiekunCreate(forms.ModelForm):

    class Meta:
        model = SalaOpiekun
        fields = '__all__'