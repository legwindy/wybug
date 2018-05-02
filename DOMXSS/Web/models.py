#!coding:utf-8

from __future__ import unicode_literals
from django.db import models

# Create your models here.

class user(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class query(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=20)

class queryhistoy(models.Model):
    name = models.CharField(max_length=30)


