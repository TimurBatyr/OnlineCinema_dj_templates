from rest_framework import serializers

from .models import AboutUs, ImageAboutUs, News, Help, ImageHelp, PublicOffer


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAboutUs
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        exclude = ('id',)


class ImageHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageHelp
        exclude = ('id',)


class PublicOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicOffer
        exclude = ('id',)


