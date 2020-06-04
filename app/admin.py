from django.contrib import admin
from .models import Sala, OpiekunSali, Rezerwacja, RezerwacjaStanowiska, RodzajSali, Rola, Stanowisko, Uzytkownik, SalaOpiekun
#from . models import users

#admin.site.register(users)


admin.site.register(Sala)
admin.site.register(OpiekunSali)
admin.site.register(Rezerwacja)
admin.site.register(RezerwacjaStanowiska)
admin.site.register(RodzajSali)
admin.site.register(Rola)
admin.site.register(Stanowisko)
admin.site.register(Uzytkownik)
admin.site.register(SalaOpiekun)