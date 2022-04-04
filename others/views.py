from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AboutUs, News, Help, ImageHelp, PublicOffer, Slider
from .serializers import AboutUsSerializer, NewsSerializer, ImageHelpSerializer, HelpSerializer, PublicOfferSerializer, \
    SliderSerializer


@api_view(['GET'])
def about_us(request):
    """О нас"""
    about_us = AboutUs.objects.all()
    serializer = AboutUsSerializer(about_us, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def news(request):
    """Новости"""
    news = News.objects.all()[:8]
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


class HelpView(generics.ListCreateAPIView):
    """Помощь"""
    queryset = Help.objects.all()

    def get(self, request):
        get_image = ImageHelp.objects.first()
        image = ImageHelpSerializer(get_image)
        queryset = Help.objects.all()
        serializers = HelpSerializer(queryset, many=True)
        return Response([image.data, serializers.data])


class PublicOfferView(generics.ListCreateAPIView):
    """Публичная оферта"""
    queryset = PublicOffer.objects.all()
    serializer_class = PublicOfferSerializer


class SliderViewSet(viewsets.ModelViewSet):
    """Слайдер"""
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


