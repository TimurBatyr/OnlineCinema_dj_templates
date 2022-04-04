from rest_framework import serializers

from .models import AboutUs, ImageAboutUs, News, Help, ImageHelp, PublicOffer, Slider


class AboutUsSerializer(serializers.ModelSerializer):
    """О нас"""
    class Meta:
        model = AboutUs
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation


class ImageSerializer(serializers.ModelSerializer):
    """О нас"""
    class Meta:
        model = ImageAboutUs
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    """Новости"""
    class Meta:
        model = News
        exclude = ('id',)


class HelpSerializer(serializers.ModelSerializer):
    """Помощь"""
    class Meta:
        model = Help
        exclude = ('id',)


class ImageHelpSerializer(serializers.ModelSerializer):
    """Фотография для помощи"""
    class Meta:
        model = ImageHelp
        exclude = ('id',)


class PublicOfferSerializer(serializers.ModelSerializer):
    """Публичная оферта"""
    class Meta:
        model = PublicOffer
        exclude = ('id',)


class SliderSerializer(serializers.ModelSerializer):
    """Слайдер"""
    class Meta:
        model = Slider
        exclude = ('id',)
