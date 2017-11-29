from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^get/subs/(?P<sem>[0-9]+)', views.getlinks),
    # url(r'^get/infos/(?P<sem>[0-9]+)', views.getinfos)
    url(r'^login/', views.login),
    url(r'^authorize', views.authorize),
    url(r'^home/', views.home, name='home'),
    url(r'^validate/', views.validate, name='validate'),
    url(r'^isauthorized/', views.isauthorized, name='isauthorized'),
    url(r'^', views.index)

]
