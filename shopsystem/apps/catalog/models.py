from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.AutoField(primary_key=True, unique=True, null=False)#�û�id����������
    userName = models.CharField(max_length=20, unique=True, null=False)#�û���
    password = models.CharField(max_length=50, null=False)#�û�����
    #�û��˺��ǲ���Ӧ���� account
    #�û��ĵȼ�
    registerTime = models.DateTimeField(auto_now=True, null=False)
    loginTime = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = "db_user"

