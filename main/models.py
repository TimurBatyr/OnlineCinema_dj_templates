from django.core.exceptions import ValidationError
from django.db import models

from ckeditor.fields import RichTextField
from colorful.fields import RGBColorField

from online_shop import settings


class Colors(models.Model):
    """Цвета для товаров"""
    name = models.CharField(max_length=50)
    color = RGBColorField()

    def __str__(self):
        return self.name


class Collection(models.Model):
    """Колллекция"""
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'ID {self.id} : {self.name}'

    class Meta:
        ordering = ['id']


class Product(models.Model):
    """Товар"""
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


class ImageProduct(models.Model):
    """Фотографии для товара"""
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='images')


class CartItem(models.Model):
    """Корзина/товары"""
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, null=True)
    cart_item_color = models.ForeignKey(Colors, on_delete=models.CASCADE, related_name='cart_item_color')
    image = models.CharField(max_length= 50, null=True)
    price = models.IntegerField(null=True, blank=True, default=0)
    old_price = models.PositiveIntegerField(null=True, blank=True)
    qty = models.PositiveSmallIntegerField(default=1)
    final_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
         return f'{self.product.name} : {self.qty} pcs'

    def save(self, *args, ** kwargs):
        product = Product.objects.get(pk=self.product_id)
        self.size = product.size
        self.price = product.price
        self.old_price = product.old_price
        self.final_price = self.qty * self.price
        self.image = product.images.first()
        super().save(*args, **kwargs)


class Cart(models.Model):
    user = models.OneToOneField('UserInfo', null=True, on_delete=models.CASCADE)
    size_line_number = models.IntegerField(null=True)
    products_quantity = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)
    sale = models.IntegerField(null=True)
    total_price_after_sale = models.IntegerField(null=True)

    def str(self):
        return self.user.name


class UserInfo(models.Model):
    """Информация юзера"""
    OrderStatus = (
        ('New', 'New'),
        ('Ordered', 'Ordered'),
        ('Canceled', 'Canceled'))
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=OrderStatus, default=OrderStatus[0])

    def __str__(self):
         return f'{self.name} : {self.created_at} : {self.status}'


class Favorite(models.Model):
    """Избранное"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_related')

    def __str__(self):
        return f'{self.product.favorites} - {self.product}'


