from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import AboutUs
from .serializers import AboutUsSerializer


@api_view(['GET'])
def about_us(request):
    about_us = AboutUs.objects.all()
    serializer = AboutUsSerializer(about_us, many=True)
    return Response(serializer.data)


