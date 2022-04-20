from django.core.exceptions import ValidationError
from django.db import models

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

class Colors(models.Model):
    """Цвета для товаров"""
    color = ColorField(default='#FF0000')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.color} - {self.name}'


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
    colors = models.ManyToManyField(Colors, related_name='product', blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING, blank=True)
    image_cart = models.ImageField(upload_to='images', blank=True)


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
    cart_item_color = models.ForeignKey(Colors, on_delete=models.DO_NOTHING, related_name='cart_item_color')
    image = models.ImageField(upload_to='images', null=True)
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
        self.image = product.image_cart
        super().save(*args, **kwargs)


class Cart(models.Model):
    """Корзина"""
    user = models.OneToOneField('UserInfo', null=True, on_delete=models.CASCADE)
    size_line_qty = models.IntegerField(null=True)
    products_qty = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        if self.id:
            cart_item = CartItem.objects.all().filter(cart_id=self.id)
            self.size_line_qty = cart_item.count()
            self.products_qty = self.size_line_qty * 5
            self.discount = (sum([i.old_price for i in cart_item]) - sum([i.price for i in cart_item])) * sum([i.qty for i in cart_item])
            self.price = sum([i.old_price for i in cart_item]) * sum([i.qty for i in cart_item])
            self.total_price = self.price - self.discount
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.name} - Корзина № {self.id}- количество линеек {self.size_line_qty}'

    def user_details(self):
        result = {
            'Name': self.user.name,
            'Last name': self.user.last_name,
            'Email': self.user.email,
            'Phone': str(self.user.phone),
            'Country': self.user.country,
            'City': self.user.city
        }
        return result


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


