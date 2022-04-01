from rest_framework import serializers

from .models import Colors, Collection, Product, Image



class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('name',)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'name', 'image',)


class ProductSerializer(serializers.ModelSerializer):
    colors = ColorsSerializer(read_only=True, many=True)
    collection = CollectionSerializer()

    class Meta:
        model = Product
        fields = ('collection', 'name', 'item_number', 'colors', 'price', 'old_price', 'description', 'size',
                  'material_composition', 'quantity_line', 'material', 'favorites',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation


class SimilarProductSerializer(ProductSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'old_price', 'discount', 'size', 'colors', 'favorites',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all()[:1], many=True, context=self.context).data
        return representation


class CollectionProductSerializer(SimilarProductSerializer):
    pass
    # class Meta:
    #     model = Product
    #     fields = ('id', 'name', 'price', 'old_price', 'discount', 'size', 'colors', 'favorites',)
    #
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['images'] = ImageSerializer(instance.images.all()[:1], many=True, context=self.context).data
    #     return representation


class NewProductSerializer(SimilarProductSerializer):
    pass



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'





