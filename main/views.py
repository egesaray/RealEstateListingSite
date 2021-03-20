from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'main/homepage.html')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def list(request):
    return render(request, 'main/list.html')

def createpost(request):
    return render(request, 'main/createpost.html')