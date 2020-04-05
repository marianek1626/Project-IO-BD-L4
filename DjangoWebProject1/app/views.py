"""
Definition of views.
"""
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
   # return HttpResponse('domek.html')
   return render(request,'homepage.html')

def about(request):
   # return HttpResponse('about')
   messages.success(request, "udalo sie zaladowac strone!");
   return render(request,'secondpage.html')
