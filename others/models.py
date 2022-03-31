from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    header = models.CharField(max_length=100)
    description = RichTextField()


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='images')


class News(models.Model):
    header = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='images')



