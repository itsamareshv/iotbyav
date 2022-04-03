"""IOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from monitor.views import *
from monitor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('monitor.urls')),
    path('home',index),
     path('delete_iot/<int:device_id>', views.delete_iot),
     path('addiot',addiot),
     path('newiot',newiot),
     path('fake',views.populate),
     path('submit',submit),
     path('email',smtp_sendmail),
     path('login',login),
     path('loggedin',loggedin),
     path('loginpage',loginpage),
     url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
