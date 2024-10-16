from django.shortcuts import render
from django.contrib.auth import logout

def homepage(request):
    logout(request)
    return render(request, 'homepage/home_page.html')
