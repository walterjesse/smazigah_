"""
URL configuration for Smazigah project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path
from django.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Smazigah1 import views

urlpatterns = [
    path('Mazigah/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('forgot/', views.forgot, name='forgot'),
    path('login/', include('login.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout/', views.logout_view, name='logout'),

]

urlpatterns += staticfiles_urlpatterns()
