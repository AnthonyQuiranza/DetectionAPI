from datetime import datetime
from sys import maxsize
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, URLField

# Create your models here.
class Test_img(models.Model):
    url= models.URLField(max_length=200)

class Result_img(models.Model):
    url = models.URLField(max_length=200)
    disease_name = models.CharField(max_length=50)
