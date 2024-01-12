from django.urls import path
from django.shortcuts import render 
from . import views
from django.conf import settings 
from django.conf.urls.static import static




app_name = 'home'
urlpatterns = [
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
