from django.conf.urls import url, include
from django.contrib import admin
from serverweb import views

urlpatterns = [
    # url(r'^get/subs/(?P<sem>[0-9]+)', views.getlinks),
    # url(r'^get/infos/(?P<sem>[0-9]+)', views.getinfos)
    url(r'^get/subjects', views.subjects),
    url(r'^submit', views.submit, name="submit"),
    url(r'^end', views.endsession, name="endsession"),
    url(r'^', views.index)

]
