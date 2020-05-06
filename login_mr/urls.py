from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('login/', views.login),
    path('profile/', views.profile),
    path('profile/maps/' ,views.map),
    path('profile/final/', views.final)
]
