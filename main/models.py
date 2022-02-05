from django.db import models
# from django.shortcuts import render
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=40, verbose_name="Называния")
    description = models.CharField(max_length=250, verbose_name="Описания")
    sent_at = models.DateTimeField(auto_now_add=True)