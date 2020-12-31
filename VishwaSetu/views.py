from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
    context = dict({})
    return render(request, 'home.html',context)

def profile(request):
    return HttpResponse("Sample Profile Page")

def globalTrending(request):
    return HttpResponse("Global Trending page")