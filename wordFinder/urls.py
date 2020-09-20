from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', csrf_exempt(views.initializeTrie), name='initializeTrie'),            
    path('checkWord/<str:word>', csrf_exempt(views.checkForWord), name='checkForWord'),
    path('startLetter/<str:letter>',csrf_exempt(views.wordStartsWithLetter),name="checkForStartLetter"),    
]
