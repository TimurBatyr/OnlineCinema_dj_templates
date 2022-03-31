from django.db import models

from ckeditor.fields import RichTextField

from colorful.fields import RGBColorField
from django.utils.text import slugify


class Colors(models.Model):
    name = models.CharField(max_length=50)
    color = RGBColorField()

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'ID {self.id} : {self.name}'

    class Meta:
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=100)
    item_number = models.CharField(max_length=100)
    price = models.PositiveIntegerField(blank=True)
    old_price = models.PositiveIntegerField(null=True, blank=True)
    discount = models.IntegerField(blank=True, default=0)
    description = RichTextField(max_length=1000)
    size = models.CharField(max_length=50)
    material_composition = models.CharField(max_length=100)
    quantity_line = models.PositiveSmallIntegerField(default=0)
    material = models.CharField(max_length=100)
    favorites = models.BooleanField(default=False)
    bestseller = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    colors = models.ManyToManyField(Colors, related_name='product')
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING, null=True, blank=True)

    def clean(self):
        if self.discount and self.old_price:
            self.price = int(self.old_price * (100 - self.discount) / 100)
        else:
            self.price = self.old_price
            self.old_price = 0

    def __str__(self):
        return f'ID {self.id} : {self.name}'


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='images')


# class Favorites(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='favorites')
#     favorites = models.BooleanField(default=True)
