from django import forms
from django.contrib import admin
from .models import AboutUs, Image


class ImageInLine(admin.TabularInline):
    model = Image
    max_num = 3
    min_num = 1


@admin.register(AboutUs)
class AboutUSAdmin(admin.ModelAdmin):
    inlines = [ImageInLine, ]


