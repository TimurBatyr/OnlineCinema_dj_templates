from django.core.exceptions import ValidationError
from django.db import models

from django.core.validators import FileExtensionValidator

from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    """О нас"""
    header = models.CharField(max_length=100)
    description = RichTextField()


class ImageAboutUs(models.Model):
    """Картинки для О нас"""
    image = models.ImageField(upload_to='images')
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='images')


class News(models.Model):
    """Новости"""
    header = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.header} - {self.id}'


class Help(models.Model):
    """Помощь"""
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100, blank=True)


class ImageHelp(models.Model):
    """Фотография для помощи с ограничением"""
    image = models.ImageField(upload_to='images')

    def save(self, *args, **kwargs):
        image = ImageHelp.objects.all()
        if image.count() > 1:
            image.delete()
        super().save(*args, **kwargs)


class Excellence(models.Model):
    """Наши преимущества"""
    icon = models.FileField(upload_to='images', validators=[FileExtensionValidator(['svg', 'png'])])
    header = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.header


class PublicOffer(models.Model):
    """Публичная оферта"""
    header = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.header


class Slider(models.Model):
    """Слайдер"""
    image = models.ImageField(upload_to='images')
    link = models.URLField(blank=True)


