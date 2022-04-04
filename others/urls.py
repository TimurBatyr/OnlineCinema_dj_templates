from django.urls import path

from others import views
from others.views import HelpView, PublicOfferView

urlpatterns = [
    path('aboutus/', views.about_us), #URL для О нас
    path('news/', views.news), #URL для новостей
    path('help/', HelpView.as_view()), #URL для помощи
    path('publicoffer/', PublicOfferView.as_view()), #URL для публичной оферты
]