import random

from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product, ImageProduct, Collection, Colors, CartItem, UserInfo, Cart, Favorite
from .serializers import ProductSerializer, ImageSerializer, CollectionSerializer, ColorsSerializer, \
    SimilarProductSerializer, CollectionProductSerializer, NewProductSerializer, BestsellerSerializer, \
    UserInfoSerializer, FavoriteSerializer, CartItemSerializer, CartSerializer, LatestSerializer, FavoriteListSerializer


class Pagination(PageNumberPagination):
    """Пагинация"""
    def get_paginated_response(self, data):
        return super().get_paginated_response(data)


class SearchProductPagination(Pagination):
    """Пагинация для поиска товаров"""
    page_size = 12


class ProductViewSet(viewsets.ModelViewSet):
    """Товар"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    pagination_class = SearchProductPagination


@api_view(['GET'])
def filter(request, name):
    """Схожие товары по категории"""
    collection = Collection.objects.get(name=name)
    queryset = Product.objects.filter(collection=collection)[0:5]
    serializer = SimilarProductSerializer(queryset, many=True)
    return Response(serializer.data)


class ImagesViewSet(viewsets.ModelViewSet):
    """Фотографии для товара"""
    queryset = ImageProduct.objects.all()
    serializer_class = ImageSerializer


class CollectionPagination(Pagination):
    """Пагинация для Коллекции"""
    page_size = 8


class CollectionViewSet(viewsets.ModelViewSet):
    """Коллекция"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = CollectionPagination


class CollectionProductPagination(Pagination):
    """Колллекция для пагинации товаров"""
    page_size = 12


class CollectionProductView(generics.ListCreateAPIView):
    """Коллекция товаров"""
    queryset = Product.objects.all()
    pagination_class = CollectionProductPagination

    def list(self, request, pk):
        queryset = Product.objects.filter(collection=pk)
        serializer = CollectionProductSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class ColorsViewSet(viewsets.ModelViewSet):
    """Цвета товаров"""
    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer


@api_view(['GET'])
def new_products(request):
    """Новинки товаров"""
    new_products = Product.objects.all().filter(new=True)[0:5]
    serializer = NewProductSerializer(new_products, many=True)
    return Response(serializer.data)


class BestsellerViewSet(viewsets.ModelViewSet):
    """Хит продаж"""
    queryset = Product.objects.all().filter(bestseller=True)
    serializer_class = BestsellerSerializer
    pagination_class = CollectionPagination


class LatestViewSet(viewsets.ModelViewSet):
    """Новинки на главной странице: пагинация 8шт, фронтэндщики сделают список по 4 шт"""
    queryset = Product.objects.all().filter(new=True)
    serializer_class = LatestSerializer
    pagination_class = CollectionPagination


class CollectionMainPageViewSet(CollectionViewSet):
    """Коллекция на главной странице: пагинация 8шт, фронтэндщики сделают список по 4 шт"""
    pass


class CartItemViewSet(viewsets.ModelViewSet):
    """Корзина инфо товары. Удаление при запросе Delete"""
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    """Корзина"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class UserInfoView(generics.CreateAPIView):
    """Информация Юзера"""
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    """Избранное"""
    queryset = Product.objects.all()
    serializer_class = FavoriteSerializer
    pagination_class = CollectionProductPagination


class FavoriteListViewSet(viewsets.ModelViewSet):
    """Избранное пост запрос"""
    queryset = Favorite.objects.all()
    serializer_class = FavoriteListSerializer


@api_view(['GET'])
def search_product(request):
    """При поиске если нет совпадений. 5 товаров с каждой категории по одной"""
    item = []
    categories = Collection.objects.all().count()
    if categories >= 5:
        for collection in Collection.objects.all().values_list('id')[0:5]:
            if Product.objects.order_by('?').filter(collection=collection).first() is None:
                pass
            else:
                item.append(random.choice(Product.objects.all().filter(collection=collection)))
    else:
        for collection in Collection.objects.all().values_list('id')[0:categories]:
            if Product.objects.order_by('?').filter(collection=collection).first() is None:
                pass
            else:
                item.append(random.choice(Product.objects.all().filter(collection=collection)))
    serializer = SimilarProductSerializer(item, many=True)
    return Response(serializer.data)

