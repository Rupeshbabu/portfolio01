from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=2083)
    image = models.FileField(upload_to='static/images/')
    status = models.IntegerField()
    upload_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
    title = models.CharField(max_length=255)
    technologies = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='static/images/')
    status = models.BooleanField(default=True)
    upload_at = models.DateTimeField(auto_now=True)


class Service(models.Model):
    title = models.CharField(max_length=255)
    fav_icon = models.FileField(upload_to='static/images', help_text='Please upload image size is <b>50 X 50 </b> only.')
    content = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    upload_at = models.DateTimeField(auto_now=True)
