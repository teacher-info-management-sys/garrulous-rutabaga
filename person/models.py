from django.db import models
from django.contrib import admin
class Yonghu(models.Model):
    Number=models.CharField(max_length=20,primary_key=True)
    Password=models.CharField(max_length=20)
    Leibie=models.CharField(max_length=10)
    def __unicode__(self):
        return self.Number
class Teacher(models.Model):
    Number=models.ForeignKey(Yonghu)
    Name=models.CharField(max_length=20)
    Profession=models.CharField(max_length=20)
    Research=models.CharField(max_length=1000)
    Education=models.CharField(max_length=1000)
    Work=models.CharField(max_length=1000)
    Information=models.CharField(max_length=2500)
    Foundation=models.CharField(max_length=20)
    Tel=models.CharField(max_length=20)
    Position=models.CharField(max_length=100)
    Rfield=models.CharField(max_length=1000)
    Rongyu=models.CharField(max_length=1000)
    Jianzhi=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.Name
class Log(models.Model):
    Number=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Event=models.CharField(max_length=100)
    def __unicode__(self):
        return self.Number
class Student(models.Model):
    Number=models.ForeignKey(Yonghu)
    Name=models.CharField(max_length=20)
    Profession=models.CharField(max_length=20)
    Tel=models.CharField(max_length=20)
    Xuenian=models.CharField(max_length=20)
    def __unicode__(self):
        return self.Name
admin.site.register(Yonghu)       
admin.site.register(Teacher)   
admin.site.register(Log)        
admin.site.register(Student)    