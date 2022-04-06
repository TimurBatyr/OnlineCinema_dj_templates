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


admin.site.register(News)
admin.site.register(Help)
admin.site.register(ImageHelp)
admin.site.register(Excellence)
admin.site.register(PublicOffer)
admin.site.register(Slider)
admin.site.register(Header)
admin.site.register(Footer)
admin.site.register(AdminContacts)
admin.site.register(CallBack)


