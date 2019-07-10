from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contacts/',views.contacts, name='contacts'),
    path('ali_weds/',views.wedding, name='wedding'),
    path('invitees/',views.getinvite, name='getinvite'),



]
