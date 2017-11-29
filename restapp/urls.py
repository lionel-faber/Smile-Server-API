from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^get/subs/(?P<sem>[0-9]+)', views.getlinks),
    url(r'^get/infos/(?P<sem>[0-9]+)', views.getinfos)
]
