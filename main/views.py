from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, viewsets, status

# from .filters import ProductFilter
from rest_framework.decorators import action, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product, Image, Collection, Colors
from .serializers import ProductSerializer, ImageSerializer, CollectionSerializer, ColorsSerializer, \
    SimilarProductSerializer, CollectionProductSerializer, NewProductSerializer


class Pagination(PageNumberPagination):

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)


class CollectionPagination(Pagination):
    page_size = 8


class CollectionProductPagination(Pagination):
    page_size = 12


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    serializer_class = SimilarProductSerializer
    # filter_backends = [DjangoFilterBackend]
    # # filterset_fields = ['collection', ]
    # filterset_class = ProductFilter


@api_view(['GET'])
def filter(request, name):
    collection = Collection.objects.get(name=name)
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
    pagination_class = CollectionPagination


class CollectionProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    pagination_class = CollectionProductPagination

    def list(self, request, pk):
        queryset = Product.objects.filter(collection=pk)
        serializer = CollectionProductSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
        #return Response(serializer.data)


class ColorsViewSet(viewsets.ModelViewSet):
    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer


@api_view(['GET'])
def new_products(request):
    new_products = Product.objects.all().filter(new=True)[0:5]
    serializer = NewProductSerializer(new_products, many=True)
    return Response(serializer.data)


