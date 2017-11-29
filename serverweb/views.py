# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
def index(request):
    return render(request, 'serverweb/index.html')

def login(request):
    return render(request, 'serverweb/login.html')

def authorize(request):
    return render(request, 'serverweb/authorize.html', { "message": "Almost there!"})

@csrf_exempt
def isauthorized(request):
    email = request.POST.get('email')
    s = Student.objects.get(email=email)
    if(s is not None):
        print s
        return HttpResponse('success')

def validate(request):
    password = request.POST.get('password')
    semester = request.POST.get('semester')
    name = request.POST.get('name')
    email = request.POST.get('email')
    valid = 'keepsmiling'
    if(password == valid):
        student = Student(name = name, email = email, semester = semester)
        student.save()
        return redirect('home')
    else:
        return render(request, 'serverweb/authorize.html', { "message": "Oops! Let's try that again."})

def home(request):
    return render(request, 'serverweb/home.html')
