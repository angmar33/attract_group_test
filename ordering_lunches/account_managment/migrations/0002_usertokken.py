# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_managment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTokken',
            fields=[
                ('user_tokken', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account_managment.User')),
            ],
        ),
    ]