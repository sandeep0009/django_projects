from django.db import models

# Create your models here.

class Users(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField(max_length=300,unique=True)
