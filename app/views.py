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
    if  request.user is None:
        return redirect('login')
    else:
        print(request.user)
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

def check_user(request):
    if request.user.is_authenticated:
        return render(request,'app/index.html')
    else:
        return render(request,'app/subpages/beforeLogin/index.html')

def check_user_pracownie(request):
    if request.user.is_authenticated:
        return render(request,'app/subpages/afterLogin/pracownie.html')
    else:
        return render(request,'app/subpages/beforeLogin/pracownie.html')

choose_place = 1

def loginPage(request):
	#if request.user.is_authenticated:
	#	return redirect('login')
	#else:
		global x
		if request.method == 'POST':

			url = 'https://fakepci.herokuapp.com/login'
			username = request.POST.get('username')
			password = request.POST.get('password')
			username1 = 'admin11@o2.pl'
			password1 = 'admin11'
			password1 = hashlib.sha512(password1.encode()).hexdigest()
			params = {'login':username1,'password':password1}
			#r = requests.post(url,params=params)
			#print(username)
			#print(password)
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
			#print(request.user.is_authenticated)
			#print(user)
			#if not request.user.is_authenticated:
			#    return render(request, 'accounts/register.html')
			if user is not None:
				 x = user.id_uzytkownika
				 #print('OKEJ')
				 login(request, user)
				 #print(request.user.is_authenticated)
				 #print(user.id_roli)
				 temp_user = user.id_roli
				 rola = Rola()
				 rola.id_roli = 2
				 if temp_user == rola:
				    return redirect('adminpage')
				 else:
				    return redirect('sale')
			else:
				messages.info(request, 'Nieprawidłowa nazwa użytkownika lub hasło!')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('index')

def event(request):
    #print(request.user.is_authenticated)
    if  not request.user.is_authenticated:
        return redirect('login')

    all_events = RezerwacjaStanowiska.objects.all()

    if request.GET:

        event_arr = []

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
        "events": all_events
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

#def default(o):
#    if hasattr(o, 'to_json'):
#        return o.to_json()
#    raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')


def pick_pila_ukosowa(request):
         #array=[]
         global choose_place
         choose_place = request.GET.get("i", None)
         #choose_place = ord(choose_place)
         global pila_ukosowa_id
         pila_ukosowa_id = Stanowisko.objects.get(nazwa_stanowiska="Piła ukosowa").id_stanowiska
         print(pila_ukosowa_id)
         #data= {"id_stanowiska": pila_ukosowa_id}
         #array.append(data)
         #print(array)
         #return JsonResponse(json.dumps(array),safe=False)
         data = {}
         return JsonResponse(data)

def pick_wiertarka_stolowa(request):
         #array=[]
         global choose_place
         choose_place = request.GET.get("i", None)
         global wiertarka_stolowa_id
         wiertarka_stolowa_id = Stanowisko.objects.get(nazwa_stanowiska="Wiertarka stołowa").id_stanowiska
         print(wiertarka_stolowa_id)
         #data= {"id_stanowiska": pila_ukosowa_id}
         #array.append(data)
         #print(array)
         #return JsonResponse(json.dumps(array),safe=False)
         data = {}
         return JsonResponse(data)

def pick_mini_szlifierka(request):
         #array=[]
         global mini_szlifierka_id
         global choose_place
         choose_place = request.GET.get("i", None)
         mini_szlifierka_id = Stanowisko.objects.get(nazwa_stanowiska="Mini szlifierka").id_stanowiska
         print(mini_szlifierka_id)
         #data= {"id_stanowiska": pila_ukosowa_id}
         #array.append(data)
         #print(array)
         #return JsonResponse(json.dumps(array),safe=False)
         data = {}
         return JsonResponse(data)

def pick_frezarka_gornowrzecinowa(request):
         #array=[]
         global frezarka_gornowrzecinowa_id
         global choose_place
         choose_place = request.GET.get("i", None)
         frezarka_gornowrzecinowa_id = Stanowisko.objects.get(nazwa_stanowiska="Frezarka górnowrzecinowa").id_stanowiska
         print(frezarka_gornowrzecinowa_id)
         #data= {"id_stanowiska": pila_ukosowa_id}
         #array.append(data)
         #print(array)
         #return JsonResponse(json.dumps(array),safe=False)
         data = {}
         return JsonResponse(data)

def pick_przecinarka_do_metalu(request):
         #array=[]
         global przecinarka_do_metalu_id
         global choose_place
         choose_place = request.GET.get("i", None)
         przecinarka_do_metalu_id = Stanowisko.objects.get(nazwa_stanowiska="Przecinarka do metalu").id_stanowiska
         print(przecinarka_do_metalu_id)
         #data= {"id_stanowiska": pila_ukosowa_id}
         #array.append(data)
         #print(array)
         #return JsonResponse(json.dumps(array),safe=False)
         data = {}
         return JsonResponse(data)

def pick_majsterkowicz(request):
         #array=[]
         global majsterkowicz_id
         global choose_place
         choose_place = request.GET.get("i", None)
         majsterkowicz_id = Stanowisko.objects.get(nazwa_stanowiska="Majsterkowicz, rzemieślnik").id_stanowiska
         print(majsterkowicz_id)
         #data= {"id_stanowiska": pila_ukosowa_id}
         #array.append(data)
         #print(array)
         #return JsonResponse(json.dumps(array),safe=False)
         data = {}
         return JsonResponse(data)

def add_event(request):
    #events_all = Rezerwacja.objects.all()
    title = request.GET.get("title", None)
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    print(start)
    print(end)
    #user = Uzytkownik.objects.get(email=request.user.email)
 
    #form = AddEventForm() 

    #print("Choose place: " + choose_place)
    global choose_place_final
    if choose_place == '0':
        choose_place_final = pila_ukosowa_id
    elif choose_place== '1':
        #print("okej")
        choose_place_final = wiertarka_stolowa_id
    elif choose_place== '2':
        choose_place_final = mini_szlifierka_id
    elif choose_place== '3':
        choose_place_final = frezarka_gornowrzecinowa_id
    elif choose_place== '4':
        choose_place_final = przecinarka_do_metalu_id
    elif choose_place== '5':
        choose_place_final = majsterkowicz_id
    else:
        print("Błąd")

    current_user = request.user
    #print("Wybor ostateczny: " + str(choose_place_final))
    #print(current_user.id_uzytkownika)
    user = Uzytkownik()
    #user.id_uzytkownika=request.user.id_uzytkownika
    user.id_uzytkownika=current_user.id_uzytkownika
    event1 = Rezerwacja.objects.create(
        id_uzytkownika = user,
        czy_anulowana = False
        )
    #print(event1)
    event1.save()

    booking = Rezerwacja.objects.get(id_rezerwacji=event1.id_rezerwacji)
    #booking.id_rezerwacji=1
    #print(booking)
    #place_test = {}
    #place_json = pick_pila_ukosowa(request)
    #a = pick_pila_ukosowa(request)
    #place_json = json.dumps(a, default = default)
    #print(pila_ukosowa_id)
    #print(place_json)
    #place_data = json.loads(place_json)
    #print(place_data)
    place = Stanowisko()
    place.id_stanowiska=choose_place_final
    #pila_ukosowa_id = Stanowisko.objects.get(nazwa_stanowiska="Piła ukosowa").id_stanowiska
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
    #print(event)
    #print(x)
    #current_user = request.user
    #print(current_user.id_uzytkownika)
    
    data = {}
    return JsonResponse(data)





def sale(request):
   pracownia = Sala.objects.all()
   #sale_list = serializers.serialize('json', sale)
    #return HttpResponse(sale_list, content_type="text/json-comment-filtered")
   return render(request, 'app/subpages/beforeLogin/pracownie.html', {'pracownie': pracownia})

def sale_login(request):
   pracownia = Sala.objects.all()
   #sale_list = serializers.serialize('json', sale)
    #return HttpResponse(sale_list, content_type="text/json-comment-filtered")
   return render(request, 'app/subpages/afterLogin/pracownie.html', {'pracownie': pracownia})

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

def rezerwacjestanowiska(request):
    rezerwacjestanowiska = RezerwacjaStanowiska.objects.all()
    user = Uzytkownik.objects.filter(id_uzytkownika=x)
    return render(request, 'app/rezerwacje.html', {'rezerwacjestanowiska': rezerwacjestanowiska, 'user':user})

def updaterezstan(request, id_rezerwacja):
    rezerwacjestanowiska = RezerwacjaStanowiska.objects.all()
    user = Uzytkownik.objects.filter(id_uzytkownika=x)
    id_rez = int(id_rezerwacja)
    try:
        rez = RezerwacjaStanowiska.objects.get(id_rezerwacji_stanowiska = id_rez)
    except RezerwacjaStanowiska.DoesNotExist:
        return redirect('rezerwacje')
    if rez.czy_anulowana==False:
        rez.czy_anulowana=True
    else:
        rez.czy_anulowana=False
    rez.save()
    return render(request, 'app/rezerwacje.html', {'rezerwacjestanowiska': rezerwacjestanowiska, 'user': user})

def createrezerwacje(request):
   form = RezerwacjaCreate(requset.POST or None)
   if form.is_valid():
      form.save()
      return redirect('rezerwacje')

   return render(request, 'app/addrezerwacje.html', {'form': form})


def updaterezerwacje(request, id):
   rezrwacja = Rezerwacja.object.get(id=id)
   form = RezerwacjaCreate(request.POST or None, instace=product)

x=1
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