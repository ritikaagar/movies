from django.conf.urls import url, include
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'^$', views.login_reg),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^welcome$', views.welcome),
]