from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def wish_birthday(request):
    return render(request, 'index.html', {"name": 'Suraj'})