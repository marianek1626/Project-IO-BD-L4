"""
Definition of urls for DjangoWebProject1.
"""

from django.conf.urls import url
from django.contrib import admin
from app import views
from django.urls import include, path



#urlpatterns = [
#    url(r'^admin/',admin.site.urls),
#    url(r'^about/$',views.about),
#    url(r'^$',views.homepage),
#    ]




urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('calendar/add/', views.add_event, name='add_event'),
    #path('calendar/about/', views.test1, name='test1'),
    path('calendar/', views.event, name='calendar'),
    #path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
    #url(r'^api-auth/', include('rest_framework.urls')),
    #path('testRestConsumer',views.testRestConsumer, name='testRestConsumer'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('rezerwacje/', views.rezerwacje, name='rezerwacje'),
    path('sale/', views.sale, name='sale'),
    path('stanowiska/', views.stanowiska, name='stanowiska'),
    path('createrezerwacje/', views.createrezerwacje, name='createrezerwacje'),
    path('updaterezerwacje/<int:id>', views.updaterezerwacje, name='updaterezerwacje'),
    path('deleterezerwacje/<int:id>', views.deleterezerwacje, name='deleterezerwacje'),
    
]
