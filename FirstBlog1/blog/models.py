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

