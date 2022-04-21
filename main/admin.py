from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe

from .models import ImageProduct, Collection, Product, Colors, CartItem, UserInfo, Favorite, Cart


class ImageInLine(admin.TabularInline):
    """Таким образом ограничил фотографии"""
    model = ImageProduct
    max_num = 8
    min_num = 0


class ProductForm(forms.ModelForm):
    """Товар"""
    description = forms.CharField(widget=CKEditorWidget(), label=Product._meta.get_field('description').verbose_name)

    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        if self.cleaned_data['colors']:
            if len(self.cleaned_data.get('colors')) > 8:
                raise forms.ValidationError('Number of colors cannot exceed 8!')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInLine, ]
    form = ProductForm


admin.site.register(Collection)
admin.site.register(Colors)


class CartItemAdmin(admin.StackedInline):
    readonly_fields = ['size', 'image', 'get_image']
    model = CartItem

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    readonly_fields = ['size_line_qty', 'products_qty', 'discount', 'price', 'total_price']
    readonly_fields += ['user_details']
    inlines = [CartItemAdmin]


class UserInfoAdmin(admin.ModelAdmin):
    search_fields = ('name', 'phone', 'last_name', 'email')
    list_display = ['name', 'phone', 'last_name', 'email']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Favorite)
