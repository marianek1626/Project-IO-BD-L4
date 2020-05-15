from django.urls import path
from .views import sale, stanowiska, rezerwacje, createrezerwacje,\
    updaterezerwacje, deleterezerwacje
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:question_id>/about', views.about, name='about'),
    path('secondpage', views.about, name='secondpage'),
    path('<int:question_id>/about', views.about, name='about'),
    
]
