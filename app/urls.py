
from django.conf.urls import url
from django.contrib import admin
from app import views
from django.urls import include, path
from .models import Rezerwacja, Uzytkownik

#def add_event(request):
#     title = request.GET.get("title", none)
#     start = request.GET.get("start", none)
#     end = request.GET.get("end", none)
#    #  event = events(title=str(title), start=start, end=end)
#     event = Rezerwacja.objects.create(
#             id_rezerwacji = 50,
#             id_uzytkownika = 1,
#             event_name = title,
#             start_date = start,
#             end_date = end,
#             czy_anulowana = False,
#        )
#     event.save()
#     data = {}

def add_event(request):
    events_all = Rezerwacja.objects.all()

    #user = Uzytkownik.objects.get(email=request.user.email)

    #form = AddEventForm() 

    #if request.method == 'POST':
    #    form = AddEventForm(request.POST or None)

    #    if form.is_valid():
    event = Rezerwacja.objects.create(
                id_rezerwacji = 50,
                id_uzytkownika = 1,
                event_name=form.cleaned_data['event_name'],
                #event_comment=form.cleaned_data['event_comment'],
                #status=form.cleaned_data['status'],
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                czy_anulowana = False,
                #calendar=form.cleaned_data['calendar'],
                #added_by=user,
            )
    event.save()

urlpatterns = [
    path('calendar/', add_event, name='add_event'),
]