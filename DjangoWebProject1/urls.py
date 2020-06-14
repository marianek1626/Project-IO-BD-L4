"""
Definition of urls for DjangoWebProject1.
"""

from django.conf.urls import url
from django.contrib import admin
from app import views
from app import adminviews
from django.urls import include, path



#urlpatterns = [
#    url(r'^admin/',admin.site.urls),
#    url(r'^about/$',views.about),
#    url(r'^$',views.homepage),
#    ]




urlpatterns = [
    path('', views.check_user, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('calendar/add/', views.add_event, name='add_event'),
    path('calendar/pick_pila_ukosowa/', views.pick_pila_ukosowa, name='pick_pila_ukosowa'),
    path('calendar/pick_wiertarka_stolowa/', views.pick_wiertarka_stolowa, name='pick_wiertarka_stolowa'),
    path('calendar/pick_mini_szlifierka/', views.pick_mini_szlifierka, name='pick_mini_szlifierka'),
    path('calendar/pick_frezarka_gornowrzecinowa/', views.pick_frezarka_gornowrzecinowa, name='pick_frezarka_gornowrzecinowa'),
    path('calendar/pick_przecinarka_do_metalu/', views.pick_przecinarka_do_metalu, name='pick_przecinarka_do_metalu'),
    path('calendar/pick_majsterkowicz/', views.pick_majsterkowicz, name='pick_majsterkowicz'),
    path('calendar/', views.event, name='calendar'),
    path('admin/', admin.site.urls),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('rezerwacje/', views.rezerwacjestanowiska, name='rezerwacjestanowiska'),
    path('sale/', views.check_user_pracownie, name='sale'),
    path('sale/', views.sale_login, name='sale_login'),
    path('stanowiska/', views.stanowiska, name='stanowiska'),
    path('createrezerwacje/', views.createrezerwacje, name='createrezerwacje'),
    path('updaterezerwacje/<int:id>', views.updaterezerwacje, name='updaterezerwacje'),
    path('deleterezerwacje/<int:id>', views.deleterezerwacje, name='deleterezerwacje'),
    path('adminpage/', adminviews.adminpage, name='adminpage'),
    path('adminpage/adminuzytkownicy/', adminviews.adminuzytkownicy_retrieve, name='adminuzytkownicy'),
    path('adminpage/adminrezerwacje/', adminviews.adminrezerwacje_retrieve, name='adminrezerwacje'),
    path('adminpage/adminsale/', adminviews.adminsale_retrieve, name='adminsale'),
    path('adminpage/adminstanowiska/', adminviews.adminstanowiska_retrieve, name='adminstanowiska'),
    path('adminpage/adminopiekunowie/', adminviews.adminopiekunowie_retrieve, name='adminopiekunowie'),
    path('adminpage/adminuzytkownicy/zmienrole/<int:user_id>', adminviews.zmienrole),
    path('adminpage/adminrezerwacje/anuluj/<int:id_rez>', adminviews.anulujrezerwacje),
    path('adminpage/adminstanowiska/status/<int:id_stan>', adminviews.zmienstatus),
    path('adminpage/przydzialy/', adminviews.przydzialy, name='przydzialy'),
    path('adminpage/przydzialy/nowyprzydzial/', adminviews.nowyprzydzial, name='nowyprzydzial'),
    path('adminpage/przydzialy/przydzial_delete/<int:id_przy>', adminviews.przydzial_delete),
    path('adminpage/adminopiekunowie/nowyopiekun', adminviews.nowyopiekun, name='nowyopiekun'),
    path('adminpage/adminopiekunowie/opiekun_delete/<int:id_op>', adminviews.opiekun_delete),
    path('adminpage/adminopiekunowie/opiekun_update/<int:id_op>', adminviews.opiekun_update, name='opiekun_update'),
    path('adminpage/adminsale/nowasala', adminviews.nowasala, name='nowasala'),
    path('adminpage/adminsale/sala_delete/<int:id_sal>', adminviews.sala_delete),
    path('adminpage/adminsale/sala_update/<int:id_sal>', adminviews.sala_update, name='sala_update'),
    path('adminpage/adminstanowiska/nowestanowisko', adminviews.nowestanowisko, name='nowestanowisko'),
    path('adminpage/adminstanowiska/stanowisko_delete/<int:id_stan>', adminviews.stanowisko_delete),
    path('adminpage/adminstanowiska/stanowisko_update/<int:id_stan>', adminviews.stanowisko_update, name='stanowisko_update'),
]
