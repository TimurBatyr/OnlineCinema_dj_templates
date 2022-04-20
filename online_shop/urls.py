from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from main.views import *
from others.views import SliderViewSet, ExcellenceViewSet, AdminContactsViewSet, CallBackViewSet, NewsViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='OnlineShop',
        description='online_shop',
        default_version='v1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

router = DefaultRouter()
router.register('product', ProductViewSet) #URL для товара +id
router.register('collections', CollectionViewSet) #URL для коллекций
router.register('slider', SliderViewSet) #URL для слайдера
router.register('collections_mainpage', CollectionMainPageViewSet) #URL для коллекций на главной странице
router.register('excellence', ExcellenceViewSet) #URL для наших преимуществ на главной странице
router.register('floatingbutton', AdminContactsViewSet) #URL для плавающей кнопки
router.register('callback', CallBackViewSet) #URL для обратного звонка
router.register('cartitem', CartItemViewSet) #URL для корзины/инфо товары
router.register('cart', CartViewSet) #URL для корзины
router.register('favorite', FavoriteViewSet) #URL для избранных
router.register('favorite_list', FavoriteListViewSet) #URL для избранных
router.register('bestseller', BestsellerViewSet) #URL для хит продаж
router.register('latest', LatestViewSet) #URL для новинок на главной странице
router.register('news', NewsViewSet) #URL для новостей

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/docs/', schema_view.with_ui('swagger')),
    path('api/v1/', include('others.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/products/filter/<str:name>/', filter, name="filter"), #URL для фильтрации товаров в категории
    path('api/v1/collection/<int:pk>/', CollectionProductView.as_view()), #URL для коллекции товаров
    path('api/v1/new_products/', new_products), #URL для новинок
    path('api/v1/userinfo/', UserInfoView.as_view()), #URL для инофрмации о юзера
    path('api/v1/search_product/', search_product), #URL для 5шт товаров из коллекции при отсутствии товара в поисковике
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
