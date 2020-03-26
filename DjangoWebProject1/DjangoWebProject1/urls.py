"""
Definition of urls for DjangoWebProject1.
"""

from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^about/$',views.about),
    url(r'^$',views.homepage),   
    ]
