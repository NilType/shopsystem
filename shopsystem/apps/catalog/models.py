from django.db import models

# Create your models here.

class User(models.Model):
    UseId = models.AutoField(primary_key=True, unique=True, null=False)
    UserName = models.CharField(max_length=20, unique=True, null=False)
    password = models.CharField(max_length=50, null=False)
    registerTime = models.DateTimeField(auto_now=True, null=False)
    loginTime = models.DateTimeField(auto_now=True, null=False)
