"""schoolproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *


#declaring the required urls for the app
urlpatterns = [
    path('',home),
    # /<str:data> is the data passed by the html page
    # redirecting the data to the relevent views function
    path('register/<str:data>/', register2, name='register'),
    path('signin/<str:data>/', register2, name='signin'),
    path('registration/<str:data>/',register,name='registration'),
    path('signin2/<str:data>/',signin,name='signin2'),
    path('registration2/<str:data>',register3,name='registration2'),
    path('signin3/<str:data>',signin2,name='signin3')
    #setting the media url
]+ static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
