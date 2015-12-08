from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.AutoField(primary_key=True, unique=True, null=False)#用户id自增长类型
    userName = models.CharField(max_length=20, unique=True, null=False)#用户名
    password = models.CharField(max_length=50, null=False)#用户密码
    #用户账号是不是应该有 account
    #用户的等级
    registerTime = models.DateTimeField(auto_now=True, null=False)
    loginTime = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = "db_user"

