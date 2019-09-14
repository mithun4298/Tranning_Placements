from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class info(models.Model):
    i_username = models.ForeignKey(User, on_delete= models.CASCADE)
    i_companyimg = models.ImageField(upload_to = 'info/%Y/%m/%D', null = True)
    i_companyname = models.CharField(max_length = 70)
    i_jobtype = models.CharField(max_length = 70)
    i_joblocation = models.CharField(max_length = 40)
    i_skills = models.CharField(max_length = 500)
    i_proglang = models.CharField(max_length = 500)
    i_jobsalary = models.FloatField()
    i_jobdescriptiion = models.TextField(max_length=2000)
    i_url = models.URLField()
    

class student(models.Model):
    s_username = models.CharField(max_length = 50 ,primary_key = True)
    s_name = models.CharField(max_length = 50)
    s_semester = models.IntegerField()
    s_branch = models.CharField(max_length = 30)
    s_tenthmarks = models.FloatField()
    s_twelthmarks = models.FloatField()
    s_currentcgpa = models.FloatField()
    s_skills = models.CharField(max_length = 100)
    s_proglang = models.CharField(max_length = 300)
    s_mobno = models.CharField(max_length = 13)
    s_resume1 = models.FileField(upload_to='resume/%Y/%m/%D', default = 'resume/CRT.pdf')
    s_resume2 = models.FileField(upload_to='resume/%Y/%m/%D', default = 'resume/CRT.pdf')
