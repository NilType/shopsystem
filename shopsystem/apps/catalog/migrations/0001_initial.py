# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('useid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('userName', models.CharField(unique=True, max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('registerTime', models.DateTimeField(auto_now=True)),
                ('loginTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'db_user',
            },
        ),
    ]
