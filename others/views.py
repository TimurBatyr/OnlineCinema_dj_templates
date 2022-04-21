from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.views import Pagination
from .models import AboutUs, News, Help, ImageHelp, PublicOffer, Slider, Excellence, Header, Footer, AdminContacts, \
    CallBack
from .serializers import AboutUsSerializer, NewsSerializer, ImageHelpSerializer, HelpSerializer, PublicOfferSerializer, \
    SliderSerializer, ExcellenceSerializer, FooterSerializer, HeaderSerializer, AdminContactsSerializer, \
    CallBackSerializer


@api_view(['GET'])
def about_us(request):
    """О нас"""
    about_us = AboutUs.objects.all()
    serializer = AboutUsSerializer(about_us, many=True)
    return Response(serializer.data)


class NewsPagination(Pagination):
    """Пагинациия для новостей"""
    page_size = 8


class NewsViewSet(viewsets.ModelViewSet):
    """Новости"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination


class HelpView(generics.ListCreateAPIView):
    """Помощь"""
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
    def get(self, request):
        get_image = ImageHelp.objects.all().first()
        image = ImageHelpSerializer(get_image)
        queryset = Help.objects.all()
        serializers = HelpSerializer(queryset, many=True)
        return Response([serializers.data, image.data])


class PublicOfferView(generics.ListAPIView):
    """Публичная оферта"""
    queryset = PublicOffer.objects.all()
    serializer_class = PublicOfferSerializer


class SliderViewSet(viewsets.ModelViewSet):
    """Слайдер.Главная страница"""
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class ExcellenceViewSet(viewsets.ModelViewSet):
    """Наши преимущества на главной странице"""
    queryset = Excellence.objects.all()[0:4]
    serializer_class = ExcellenceSerializer


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 50


class HeaderFooterAPIView(ObjectMultipleModelAPIView):
    """Хэдер и Футер: модельки и сериалайзеры объеденены в одну вьюшку"""
    pagination_class = LimitPagination
    querylist = (
        {'queryset': Header.objects.all(), 'serializer_class': HeaderSerializer},
        {'queryset': Footer.objects.all(), 'serializer_class': FooterSerializer},
    )


class AdminContactsViewSet(viewsets.ModelViewSet):
    """Плавающая кнопка"""
    queryset = AdminContacts.objects.all()
    serializer_class = AdminContactsSerializer


class CallBackViewSet(viewsets.ModelViewSet):
    """Обратный звонок"""
    queryset = CallBack.objects.all()
    serializer_class = CallBackSerializer
