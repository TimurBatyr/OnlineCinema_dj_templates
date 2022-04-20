from django.contrib import admin

from .models import AboutUs, ImageAboutUs, News, Help, ImageHelp, Excellence, PublicOffer, Slider, Header, Footer, \
    AdminContacts, CallBack


class ImageAboutUsInLine(admin.TabularInline):
    model = ImageAboutUs
    max_num = 3
    min_num = 1


@admin.register(AboutUs)
class AboutUSAdmin(admin.ModelAdmin):
    inlines = [ImageAboutUsInLine, ]

    def has_add_permission(self, request):
        no_add = super().has_add_permission(request)
        if no_add and AboutUs.objects.exists():
            no_add = False
        return no_add

    class Meta:
        model = AboutUs


admin.site.register(News)
admin.site.register(Help)
admin.site.register(Excellence)


@admin.register(ImageHelp)
class ImageHelpAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        no_add = super().has_add_permission(request)
        if no_add and ImageHelp.objects.exists():
            no_add = False
        return no_add

    class Meta:
        model = ImageHelp


@admin.register(PublicOffer)
class PublicOfferAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        no_add = super().has_add_permission(request)
        if no_add and PublicOffer.objects.exists():
            no_add = False
        return no_add

    class Meta:
        model = PublicOffer


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        no_add = super().has_add_permission(request)
        if no_add and Footer.objects.exists():
            no_add = False
        return no_add

    class Meta:
        model = Footer


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        no_add = super().has_add_permission(request)
        if no_add and Header.objects.exists():
            no_add = False
        return no_add

    class Meta:
        model = Header

admin.site.register(Slider)
admin.site.register(AdminContacts)


class CallBackAdmin(admin.ModelAdmin):
    search_fields = ('name', 'phone',)
    list_display = ['name', 'phone', 'call_status', 'date_created']
    list_filter = ['call_status']


admin.site.register(CallBack, CallBackAdmin)







