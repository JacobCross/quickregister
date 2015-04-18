from django.db import models
from django import forms

# Create your models here.

class posts(models.Model):

    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()

class datapack(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=30)
    school = models.CharField(max_length=100)

class finaldata(models.Model):
    #date = models.DateTimeField(auto_now=True)
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=64)
    mname = models.CharField(max_length=32)
    dob = models.CharField(max_length=16)
    birthp = models.CharField(max_length=64)
    gender = models.CharField(max_length=32)
    genderhide = models.CharField(max_length=32)  # possibly for the 'other' text input box that appears
    soc = models.CharField(max_length=32)
    school = models.CharField(max_length=128)
    maddress = models.CharField(max_length=64)
    maddress2 = models.CharField(max_length=64)
    maddresscity = models.CharField(max_length=64)
    maddressstate = models.CharField(max_length=64)
    saddress = models.CharField(max_length=64)
    saddress2 = models.CharField(max_length=64)
    saddresscity = models.CharField(max_length=64)
    saddressstate = models.CharField(max_length=64)
    hphone = models.CharField(max_length=16)
    unlisted = models.BooleanField()
    father = models.BooleanField()
    mother = models.BooleanField()
    guardian = models.BooleanField()
    fathername = models.CharField(max_length=32)
    fatherwnum = models.CharField(max_length=32)
    fathercnum = models.CharField(max_length=32)
    mothername = models.CharField(max_length=32)
    motherwnum = models.CharField(max_length=32)
    mothercnum = models.CharField(max_length=32)