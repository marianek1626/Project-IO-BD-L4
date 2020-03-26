"""
Definition of views.
"""

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
   # return HttpResponse('domek.html')
   return render(request,'homepage.html')

def about(request):
   # return HttpResponse('about')
   return render(request,'about.html')