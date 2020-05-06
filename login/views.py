from django.shortcuts import render
#from django.http import HttpResponse



def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def scores(request):
    return render(request, 'score.html')

def maps(request):
    return render(request, 'map.html')

def final(request):
    return render(request, 'final.html')




