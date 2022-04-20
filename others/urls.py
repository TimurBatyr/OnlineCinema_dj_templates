from django.urls import path

from others import views
from others.views import HelpView, PublicOfferView, HeaderFooterAPIView


urlpatterns = [
    path('aboutus/', views.about_us), #URL для О нас
    path('help/', HelpView.as_view()), #URL для помощи
    path('publicoffer/', PublicOfferView.as_view()), #URL для публичной оферты
    path('headerfooter/', HeaderFooterAPIView.as_view()),#URL для хэдера и футера
]