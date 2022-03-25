from django.urls import path

from others import views

urlpatterns = [
    path('aboutus/', views.about_us),
]