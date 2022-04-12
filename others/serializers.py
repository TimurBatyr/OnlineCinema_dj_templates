from rest_framework import serializers

from .models import AboutUs, ImageAboutUs, News, Help, ImageHelp, PublicOffer, Slider, Excellence, Header, Footer, \
    AdminContacts, CallBack


class AboutUsSerializer(serializers.ModelSerializer):
    """О нас"""
    class Meta:
        model = AboutUs
        exclude = ('id',)

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
    """Слайдер на главной странице"""
    class Meta:
        model = Slider
        exclude = ('id',)


class ExcellenceSerializer(serializers.ModelSerializer):
    """Наши преимущества на главной странице"""

    class Meta:
        model = Excellence
        exclude = ('id',)


class HeaderSerializer(serializers.ModelSerializer):
    """Хэдер"""
    class Meta:
        model = Header
        exclude = ('id',)


class FooterSerializer(serializers.ModelSerializer):
    """Футер"""
    class Meta:
        model = Footer
        fields = ('type', 'link',)


class AdminContactsSerializer(serializers.ModelSerializer):
    """Плавающая кнопка"""
    class Meta:
        model = AdminContacts
        fields = ('type', 'link',)


class CallBackSerializer(serializers.ModelSerializer):
    """Обратный звонок"""
    date_created = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)

    class Meta:
        model = CallBack
        exclude = ('id',)
