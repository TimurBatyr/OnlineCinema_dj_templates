from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, viewsets, status

# from .filters import ProductFilter
from rest_framework.decorators import action, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product, Image, Collection, Colors
from .serializers import ProductSerializer, ImageSerializer, CollectionSerializer, ColorsSerializer, \
    SimilarProductSerializer


class MyPaginationClass(PageNumberPagination):
    page_size = 8

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    serializer_class = SimilarProductSerializer
    # filter_backends = [DjangoFilterBackend]
    # # filterset_fields = ['collection', ]
    # filterset_class = ProductFilter


@api_view(['GET'])
def filter(request, name):
    print("hello")
    collection = Collection.objects.get(name=name)
    print(collection)
    queryset = Product.objects.filter(collection=collection)[0:5]
    serializer = SimilarProductSerializer(queryset, many=True)
    return Response(serializer.data)


    #
    # @action(detail=False, methods=['get'])
    # def filter(self, request, pk=None):
    #     queryset = self.get_queryset()[0:5]
    #     collection = Collection.objects.first()
    #     queryset = queryset.filter(collection = collection.id)
    #     serializer = ProductSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data)


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = MyPaginationClass


class ColorsViewSet(viewsets.ModelViewSet):
    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer
