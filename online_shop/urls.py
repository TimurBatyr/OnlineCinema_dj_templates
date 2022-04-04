from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import *
from others.views import SliderViewSet

router = DefaultRouter()
router.register('product', ProductViewSet) #URL для товара +id
router.register('collections', CollectionViewSet) #URL для коллекций
router.register('slider', SliderViewSet) #URL для слайдера
router.register('collections_mainpage', CollectionMainPageViewSet) #URL для коллекций на главной странице


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('others.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/products/filter/<str:name>/', filter, name="filter"), #URL для фильтрации товаров в категории
    path('api/v1/collection/<int:pk>/', CollectionProductView.as_view()), #URL для коллекции товаров
    path('api/v1/new_products/', new_products), #URL для новинок
    path('api/v1/bestseller/', bestseller), #URL для хит продаж
    path('api/v1/novinki/', novinki), #URL для новинок на главной странице
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
