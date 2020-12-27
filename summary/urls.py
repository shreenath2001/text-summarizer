from os import name
from django.urls import path
from . import views
import summary

urlpatterns = [
    path('', views.home, name = 'home'),
    path('summarizer/', views.summary, name = 'summary'),
    path('learn/', views.learn, name = 'learn'),
    path('summarizer/summarizeText', views.summarizeText, name = 'summarizeText'),
    path('summarizer/summarizeUrl', views.summarizeUrl, name = 'summarizeUrl'),
    path('summarizer/summarizeImage', views.summarizeImage, name = 'summarizeImage'),
]