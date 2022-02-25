from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Plan(models.Model):
    planowner=models.CharField(max_length=50)
    title=models.CharField(max_length=150)
    dsc=models.TextField()
    price=models.IntegerField()
    
    def __str__(self):
        return self.title 
class Subscribe(models.Model):
    name=models.CharField(max_length=150)
    email=models.TextField(primary_key=True)
    mobno=models.CharField(max_length=10)
    address=models.CharField(max_length=300)
    plansubscribed=models.IntegerField()
    payment=models.BooleanField(default=False)
    date= models.DateTimeField(auto_now_add=True,null=True)

    
    def __str__(self):
        return self.name

class Reviews(models.Model):
    content=models.TextField(max_length=500)
    def __str__(self):
        return self.content

class Feedback(models.Model):
    name=models.CharField(max_length=150)
    address=models.CharField(max_length=300)
    mobile=models.CharField(max_length=10)
    content=models.TextField(max_length=500)

    def __str__(self):
        return self.name

