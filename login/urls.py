from django.urls import path, include
from login import views
from login.views import contact_form

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('contact/', contact_form, name='contact_form'),

]