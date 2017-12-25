# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from restapp.models import Subject, Link, Info
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
import json
from .models import *

# Create your views here.
@login_required(login_url="/accounts/login/")
def index(request):
    return render(request, 'serverweb/index.html')

def endsession(request):
    logout(request)
    return HttpResponseRedirect('/web')

def subjects(request):
    sem = request.POST['semester']
    result = Subject.objects.filter(semester = sem).values()
    print result
    r = list(result)
    return JsonResponse(r, safe = False)

def submit(request):
    sem = request.POST.get('semester')
    typ = request.POST.get('type')
    notif = request.POST.get('notif')
    if typ.encode('utf8') == '4':
        subject = request.POST.get('subject_title')
        notes_type = request.POST.get('notes_type')
        title = request.POST.get('notes_title')
        link = request.POST.get('notes_link')
        sub = Subject.objects.get(code = subject)
        entry = Link(subject = sub, title = title, link = link, notesType = notes_type)
        entry.save()
    elif typ.encode('utf8') != '5':
        title = request.POST.get('info_title')
        details = request.POST.get('info_details')
        date = request.POST.get('info_date')
        entry = Info(title = title, infoType = typ, semester = sem, subInfos = details, date = date)
        entry.save()
    if notif.encode('utf8') == 'yes':
        title = request.POST.get('notif_title')
        msg = request.POST.get('notif_details')
        url = 'https://fcm.googleapis.com/fcm/send'
        data = {
            "to": "/topics/semester" + sem,
            "data" : {
                "message" : msg,
                "content_available" : True,
                "priority" : "high",
                "title" : title,
                "fragment" : typ.encode('utf8')
                }
            }
        headers={'Content-Type': 'application/json', 'Authorization': 'key=AAAA9gZGmR4:APA91bGM19qwIMmhqtoJ7TUiSBR57cHzMZIg2D-5Em3pnQ72ph1iFKKTS3iZDFRp43QKvVesGEm4guCSQTSWW9DsUS2S_DwGnJ0QempQGlktjTcgXRhXPFDAXPBnVpptDIxefChrcdEC'}
        response = requests.post(url, json.dumps(data), headers = headers)
    return HttpResponseRedirect('/web')
