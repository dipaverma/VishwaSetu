from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World')

def profile(request):
    return HttpResponse("Sample Profile Page")

def globalTrending(request):
    return HttpResponse("Global Trending page")