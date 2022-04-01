from django.urls import path

from others import views
from others.views import HelpView, PublicOfferView

urlpatterns = [
    path('aboutus/', views.about_us),
    path('news/', views.news),
    path('help/', HelpView.as_view()),
    path('publicoffer/', PublicOfferView.as_view())
]