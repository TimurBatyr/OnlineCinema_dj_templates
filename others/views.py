from django.shortcuts import render
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AboutUs, News, Help, ImageHelp, PublicOffer
from .serializers import AboutUsSerializer, NewsSerializer, ImageHelpSerializer, HelpSerializer, PublicOfferSerializer


@api_view(['GET'])
def about_us(request):
    about_us = AboutUs.objects.all()
    serializer = AboutUsSerializer(about_us, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def news(request):
    news = News.objects.all()[:8]
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


class HelpView(generics.ListAPIView):
    queryset = Help.objects.all()

    def get(self, request):
        queryset = ImageHelp.objects.first()
        image = ImageHelpSerializer(queryset)
        queryset = Help.objects.all()
        serializers = HelpSerializer(queryset, many=True)
        return Response([image.data, serializers.data])


class PublicOfferView(generics.ListAPIView):
    queryset = PublicOffer.objects.all()
    serializer_class = PublicOfferSerializer



