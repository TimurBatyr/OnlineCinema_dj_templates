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


class Header(models.Model):
    """Хэдер"""
    image = models.ImageField(upload_to='images')
    infotext = RichTextField()
    phone = models.CharField(max_length=20)


"""Футер и хэдер"""
CHOICES = (
    ('Number', 'Number'),
    ('Email', 'Email'),
    ('Instagram', 'Instagram'),
    ('Telegram', 'Telegram'),
    ('Whatsapp', 'Whatsapp')
)


class Footer(models.Model):
    """Футер"""
    type = models.CharField(max_length=100, choices=CHOICES)
    link = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if self.type == 'Number':
            self.link = f'{self.link}'
        elif self.type == 'Whatsapp':
            self.link = f'https://wa.me/{self.link}'
        elif self.type == 'Email':
            self.link == f'{self.link}'
        elif self.type == 'Instagram':
            self.link = f'https://www.instagram.com/{self.link}/'
        elif self.type == 'Telegram':
            self.link = f'https://t.me/{self.link}/'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.type


class AdminContacts(models.Model):
    """Для тикета плавающей кнопки(обратный звонок)"""
    CONTACTS = (
        ('Number', 'Number'),
        ('Telegram', 'Telegram'),
        ('Whatsapp', 'Whatsapp'))
    type = models.CharField(max_length=100, choices=CONTACTS)
    link = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if self.type == 'Number':
            self.link = f'{self.link}'
        elif self.type == 'Whatsapp':
            self.link = f'https://wa.me/{self.link}'
        elif self.type == 'Telegram':
            self.link = f'https://t.me/{self.link}/'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.type


class CallBack(models.Model):
    """Обратный звонок"""
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    callback = models.BooleanField(default=True)
    call_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
