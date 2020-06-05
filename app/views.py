"""
Definition of views.
"""
from django.conf import settings
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
from django.http import JsonResponse
from .models import Sala, OpiekunSali, Rezerwacja, RezerwacjaStanowiska, RodzajSali, Rola, Stanowisko, Uzytkownik
from .forms import CreateUserForm, SalaCreate,  OpiekunSaliCreate, RezerwacjaCreate,\
    RezerwacjaStanowiskaCreate, RodzajSaliCreate, RolaCreate, StanowiskoCreate, UzytkownikCreate
import hashlib

import datetime
from django.utils.timezone import make_aware

naive_datetime = datetime.datetime.now()
naive_datetime.tzinfo  # None

settings.TIME_ZONE  # 'UTC'
aware_datetime = make_aware(naive_datetime)
aware_datetime.tzinfo  # <UTC>

from django.utils import timezone
import pytz
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

#def index(request):
 #   list = Rola.objects.order_by('id_roli')[:5]
 #   template = loader.get_template('rola.html')
 #   context = {
  #      'Rola': list,
  #  }
  #  return HttpResponse(template.render(context, request))

def index(request):
    return render(request,'app/index.html')

#def testRestConsumer(request):
#    if request.method == 'GET':



def loginPage(request):
	#if request.user.is_authenticated:
	#	return redirect('login')
	#else:
		if request.method == 'POST':

			url = 'https://fakepci.herokuapp.com/login'
			username = request.POST.get('username')
			password = request.POST.get('password')
			username1 = 'admin11@o2.pl'
			password1 = 'admin11'
			password1 = hashlib.sha512(password1.encode()).hexdigest()
			print(password1)
			params = {'login':username1,'password':password1}
			#r = requests.post(url,params=params)
			print(username)
			print(password)
			#r1 = requests.post('https://fakepci.herokuapp.com/login?login=admin11@o2.pl&password=c230e0811f617ea267bab08f8a62ca0585218cfa33676f6ed7d67b7d5af36192df3879350d5accc26a22486c8774bce92c3cfe3a3e5c9aa270cce55709db6821')
			#print(r.json())
			#password_hash = hashlib.sha512(password.encode()).hexdigest()
			#print(password_hash)
			#if Uzytkownik.objects.filter(haslo=password).exists():
			#	customUser = Uzytkownik.objects.get(haslo=password)
			#	login(request,customUser)
			#	messages.success(request,'Zalogowano poprawnie')
			#	return redirect('calendar')
			user = authenticate(request, email=username, haslo=password)
			print(user)
			#if not request.user.is_authenticated:
			#    return render(request, 'accounts/register.html')
			if user is not None:
				 print('OKEJ')
				 login(request, user)
				 return redirect('sale')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def event(request):
    all_events = RezerwacjaStanowiska.objects.all()
    #get_event_types = Rezerwacja.objects.only('event_type')
    if request.GET:
        event_arr = []
        #if request.GET.get('event_type') == "all":
        #    all_events = Rezerwacja.objects.all()
        #else:
        #    all_events = Rezerwacja.objects.filter(event_type__icontains=request.GET.get('event_type'))

        for i in all_events:
            event_sub_arr = {}
            #event_sub_arr['title'] = i.event_name
            start_date = datetime.strptime(str(i.start_date.date()), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            end_date = datetime.strptime(str(i.end_date.date()), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events": all_events,
        #"get_event_types": get_event_types,

    }
    return render(request, 'app/subpages/beforeLogin/stanowiska.html', context)

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

#def add_event2(request):
#    events_all = Rezerwacja.objects.all()
#    title = request.GET.get("title", None)
#    start = request.GET.get("start", None)
#    end = request.GET.get("end", None)

#def test1(request):

#    return render(request,'app/about.html')

def add_event(request):
    #events_all = Rezerwacja.objects.all()
    title = request.GET.get("title", None)
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    print(start)
    print(end)
    #user = Uzytkownik.objects.get(email=request.user.email)

    #form = AddEventForm() 
    
    #if request.method == 'POST':
    #    form = AddEventForm(request.POST or None)
    #user = Uzytkownik()
    #user.id_uzytkownika=1
    booking = Rezerwacja()
    booking.id_rezerwacji=1
    place = Stanowisko()
    place.id_stanowiska=1
    #    if form.is_valid():
    event = RezerwacjaStanowiska.objects.create(
                #id_rezerwacji = 47, # będzie się autoinkrementował ?
                id_rezerwacji = booking,
                id_stanowiska=place,
                termin_rozpoczecia=start,
                termin_zakonczenia=end,
                czy_anulowana = False,
            )
    event.save()
    data = {}
    return JsonResponse(data)

def sale(request):
   pracownia = Sala.objects.all()
   #sale_list = serializers.serialize('json', sale)
    #return HttpResponse(sale_list, content_type="text/json-comment-filtered")
   return render(request, 'app/subpages/beforeLogin/pracownie.html', {'pracownie': pracownia})

# return render(request, 'pracownie.html', {'pracownie': pracownia})
# sale_list = list(sale)  # important: convert the QuerySet to a list object
# serialized_obj = serializers.serialize('json', [sale_list])
# return JsonResponse(serialized_obj, safe=False)

def role(request):
   rol = Rola.objects.all()
   return render(request, 'app/pracownie.html', {'rol': rol})

def stanowiska(request):
   stanowisko = Stanowisko.objects.all()
   return render(request, 'app/subpages/beforeLogin/stanowiska.html', {'stanowiska': stanowisko})


def rezerwacje(request):
   rezerwacja = Rezerwacja.objects.all()
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

#def uzytkownicy(request):
#   user = Uzytkownik.objects.all()
#   with open('uzytkownicy.json', 'w') as outfile:
#       json.dump("uzytkownicy: ", outfile)
#   for e in user:
#       x = str(e.imie)
#       with open('uzytkownicy.json', 'a') as outfile:
#           json.dump(x, outfile)
#       x = str(e.nazwisko)
#       with open('uzytkownicy.json', 'a') as outfile:
#           json.dump(x, outfile)
#       x = str(e.email)
#       with open('uzytkownicy.json', 'a') as outfile:
#           json.dump(x, outfile)
#       x = str(e.haslo)
#       with open('uzytkownicy.json', 'a') as outfile:
#           json.dump(x, outfile)
#       x = str(e.id_roli)
#       rol = Rola.objects.all()
#       for a in rol:
#           if e.id_roli == a:
#            x = str(a.nazwa_roli)
#            with open('uzytkownicy.json', 'a') as outfile:
#                json.dump(x, outfile)
#   return render(request, 'uzytkownicy.html', {'user': user})

#  with open('rola.json', 'w') as outfile:
#     json.dump("Role: ", outfile)
  #      x = str(e.nazwa_roli)
  #      with open('rola.json', 'a') as outfile:
  #          json.dump(x, outfile)
   #messages.success(request, e);
   #return render(request, 'rola.html', "x")
 #messages.success(request, "udalo sie zaladowac strone!");

    #return HttpResponse(render, "rola")

#def czytajdane():
#    """Funkcja pobiera i wyświetla dane z bazy."""
#    rol = Rola.objects.all()
#    with open('datax.json', 'w') as outfile:
#        json.dump("Role: ", outfile)
#    for e in rol:
#        x = str(e.nazwa_roli)
#        print(x)
#        #d = json.loads(x)
#        with open('datax.json', 'a') as outfile:
#            json.dump(x, outfile)