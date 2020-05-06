from django.shortcuts import render

def index(request):
    return render(request,'indexmr.html')


def login(request):
    return render(request,'login_mr.html')


def profile(request):
    return render(request, 'profile_mr.html')


def map(request):
    return render(request, 'maps_mr.html')


def final(request):
    return render(request, 'final_mr.html')
