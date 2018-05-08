#!coding:utf-8

from __future__ import unicode_literals
from django.db import models

# Create your models here.

class user(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class commit(models.Model):
    commit = models.TextField(max_length=80)


