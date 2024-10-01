# recognize/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recognize/', views.recognize_digit, name='recognize_digit'),
]
