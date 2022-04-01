from django.core.validators import FileExtensionValidator
from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    header = models.CharField(max_length=100)
    description = RichTextField()


class ImageAboutUs(models.Model):
    image = models.ImageField(upload_to='images')
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='images')


class News(models.Model):
    header = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='images')


class Help(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100, blank=True)


class ImageHelp(models.Model):
    image = models.ImageField(upload_to='images')


class Excellence(models.Model):
    icon = models.FileField(upload_to='images', validators=[FileExtensionValidator(['svg', 'png'])])
    header = models.CharField(max_length=100)
    description = RichTextField()





