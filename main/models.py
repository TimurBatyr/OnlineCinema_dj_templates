from django.db import models


class Product(models.Model):
    pass


class Collection(models.Model):
    pass


class ProductDetail(models.Model):
    pass


class Colors(models.Model):
    pass


class Image(models.Model):
    pass
    # image = models.ImageField(upload_to='images')
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


