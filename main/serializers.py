from rest_framework import serializers

from .models import Colors, Collection, Product, ImageProduct, Cart, UserInfo


class ColorsSerializer(serializers.ModelSerializer):
    """Цвета для товаров"""
    class Meta:
        model = Colors
        fields = ('name',)


class CollectionSerializer(serializers.ModelSerializer):
    """Коллекция"""
    class Meta:
        model = Collection
        fields = ('id', 'name', 'image',)


class ProductSerializer(serializers.ModelSerializer):
    """Товар"""
    colors = ColorsSerializer(read_only=True, many=True)
    collection = CollectionSerializer()

    class Meta:
        model = Product
        fields = ('collection', 'name', 'item_number', 'colors', 'price', 'old_price', 'discount', 'description', 'size',
                  'material_composition', 'quantity_line', 'material', 'favorites',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation


class SimilarProductSerializer(ProductSerializer):
    """Товары по категории"""
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'old_price', 'discount', 'size', 'colors', 'favorites',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all()[:1], many=True, context=self.context).data
        return representation


class CollectionProductSerializer(SimilarProductSerializer):
    """Коллекция товаров"""
    pass


class NewProductSerializer(SimilarProductSerializer):
    """Новинки товаров"""
    pass


class BestsellerSerializer(SimilarProductSerializer):
    """Хит продаж"""
    pass


class NovinkiSerializer(SimilarProductSerializer):
    """Новинки на главной странце"""
    pass


class ImageSerializer(serializers.ModelSerializer):
    """Фотографии для товаров"""
    class Meta:
        model = ImageProduct
        fields = '__all__'


class ProductCartSerializer(ProductSerializer):
    """Serializer для корзины"""
    colors = ColorsSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('name', 'item_number', 'colors', 'price', 'old_price', 'size',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all()[:1], many=True, context=self.context).data
        return representation


class CartSerializer(serializers.ModelSerializer):
    """Корзина"""
    product = ProductCartSerializer()

    class Meta:
        model = Cart
        fields = "__all__"


class UserInfoSerializer(serializers.ModelSerializer):
    """Информация Юзера"""
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)

    class Meta:
        model = UserInfo
        fields = '__all__'


# class FavoritesSerializer(serializers.ModelSerializer):
#     """Избранное"""
#     class Meta:
#         model = Favorites
#         fields = ('id', 'movie', 'favorites', 'owner',)


class FavoriteSerializer(ProductSerializer):
    """Избранное"""
    class Meta:
        model = Product
        fields = ('name', 'price', 'old_price', 'discount', 'size', 'colors', 'id', 'favorites',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all()[:1], many=True, context=self.context).data
        return representation