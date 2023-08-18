from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200)
    section=models.CharField(max_length=1)
    grade=models.CharField(max_length=1)
    
    def __str__(self):
        return f'{self.name} (Section: {self.section}, Grade: {self.grade})'
    
class Veggies(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
   
    receipe_name=models.CharField(max_length=150)
    receipe_description=models.TextField()
    receipe_image=models.ImageField(upload_to='receipe')