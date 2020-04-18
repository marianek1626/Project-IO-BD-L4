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
    path('', views.homepage, name='homepage'),
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
]
