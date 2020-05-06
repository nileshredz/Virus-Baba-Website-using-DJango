from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index_hi.html')


def login(request):
    return render(request, 'login_hi.html')

def profile(request):
    return render(request, 'profile_hi.html')

def map(request):
    return render(request, 'map_hi.html')


def final(request):
    return render(request, 'final_hi.html')