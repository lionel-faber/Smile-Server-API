# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, JsonResponse
import simplejson as json
from django.core import serializers
from .models import *

def getlinks(request, sem):
    s = Subject.objects.filter(semester=sem)
    l = Link.objects.filter(subject__in=s).values()
    links = list(l)
    return JsonResponse(links, safe=False)

def getinfos(request, sem):
    s = Info.objects.filter(semester=sem).values()
    infos = list(s)
    return JsonResponse(infos, safe=False)
