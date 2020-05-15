"""
Definition of views.
"""

from django.conf.urls import url
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#import services
import requests
import json
from .models import Sala, OpiekunSali, Rezerwacja, RezerwacjaStanowiska, RodzajSali, Rola, Stanowisko, Uzytkownik
from .forms import CreateUserForm, SalaCreate,  OpiekunSaliCreate, RezerwacjaCreate,\
    RezerwacjaStanowiskaCreate, RodzajSaliCreate, RolaCreate, StanowiskoCreate, UzytkownikCreate
import hashlib
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
@cache_page(60 * 15)
@csrf_protect


def homepage(request):
   # return HttpResponse('domek.html')
   return render(request,'app/homepage.html')

def calendar(request):
    return render(request,'app/calendar.html')

def about(request):
   # return HttpResponse('about')
   messages.success(request, "udalo sie zaladowac strone!");
   return render(request,'app/secondpage.html')

def layout(request):
    return render(request,'app/MainSite.html')

#def testRestConsumer(request):
#    if request.method == 'GET':
    
def loginPage(request):
	#if request.user.is_authenticated:
	#	return redirect('login')
	#else:
		if request.method == 'GET':

			url = 'https://fakepci.herokuapp.com/login'
			username = request.POST.get('username')
			password = request.POST.get('password')
			username1 = 'admin11@o2.pl'
			password1 = 'admin11'
			password1 = hashlib.sha512(password1.encode()).hexdigest()
			print(password1)
			params = {'login':username1,'password':password1}
			r = requests.post(url,params=params)
			
			r1 = requests.post('https://fakepci.herokuapp.com/login?login=admin11@o2.pl&password=c230e0811f617ea267bab08f8a62ca0585218cfa33676f6ed7d67b7d5af36192df3879350d5accc26a22486c8774bce92c3cfe3a3e5c9aa270cce55709db6821')
			#print(r)
			print(r.json())
			#print(username)
			#print(password)
			#password_hash = hashlib.sha512(password.encode()).hexdigest()
			#print(password_hash)
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('calendar')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)





def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Konto zostało stworzone: ' + user)
            return redirect('login')

    context={'form':form}
    return render(request,'accounts/register.html',context)

#class loginPage1(generic.TemplateView):
#     def get(self,request):
#         user_list = services.check_user('')


def sale(request):
   pracownia = Sala.object.all()
   return render(request, 'app/pracownie.html', {'pracownie': pracownia})

def role(request):
   rol = Rola.object.all()
   return render(request, 'app/pracownie.html', {'rol': rol})

def stanowiska(request):
   stanowisko = Stanowisko.object.all()
   return render(request, 'app/stanowiska.html', {'stanowiska': stanowisko})


def rezerwacje(request):
   rezerwacja = Rezerwacja.object.all()
   return render(request, 'app/rezerwacje.html', {'rezerwacje': rezerwacja})


def createrezerwacje(request):
   form = RezerwacjaCreate(requset.POST or None)
   if form.is_valid():
      form.save()
      return redirect('rezerwacje')

   return render(request, 'app/addrezerwacje.html', {'form': form})


def updaterezerwacje(request, id):
   rezrwacja = Rezerwacja.object.get(id=id)
   form = RezerwacjaCreate(request.POST or None, instace=product)


def deleterezerwacje(request, id):
   rezerwacja = Rezerwacja.object.get(id=id)

   if request.method == 'POST':
      rezerwacja.delete()
      return redirect('app/deleterezerwacje')

   return render(request, 'app/deleterezerwacje.html', {'rezerwacje': rezerwacja})