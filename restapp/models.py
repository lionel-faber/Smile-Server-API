# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from jsonfield import JSONCharField

from django.db import models

# Create your models here.
class Subject(models.Model):
    code = models.CharField(max_length=10, primary_key = True)
    name = models.CharField(max_length = 50)
    semester = models.CharField(max_length = 2)
    credits = models.CharField(max_length = 2)
    def __str__(self):
        return self.name

class Link(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length = 20)
    link = models.CharField(max_length = 200)
    types = (
        ('1', 'Class Notes'),
        ('2', 'Question Bank'),
        ('3', 'Staff Notes'),
        ('4', 'Test Questions')
    )
    notesType = models.CharField(
        max_length=5,
        choices = types
    )
    def __str__(self):
        return self.title

class Info(models.Model):
    title = models.CharField(max_length = 500)
    types = (
        ('1', 'Information'),
        ('2', 'Schedule'),
        ('3', 'Placement')
    )
    infoType = models.CharField(max_length = 5, choices = types)
    semester = models.CharField(max_length = 2)
    subInfos = models.CharField(max_length = 1000, null = True, blank = True)
    date = models.DateField(auto_now=False, auto_now_add = False)
    def __str__(self):
        return self.title
