from turtle import home
from django.contrib import admin
from django.urls import path , include

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('login',include('home.urls')),
    path('purchase',include('home.urls')),
    path('register',include('home.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
]
