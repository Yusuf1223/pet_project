from django.contrib import admin
from store.models import *
# Register your models here.

admin.site.register(Feedback)
admin.site.register(Info)
admin.site.register(Contact)
admin.site.register(Right)

admin.site.register(Color)
admin.site.register(Material)
admin.site.register(WatchStyle)
admin.site.register(Coating)
admin.site.register(GlassMaterial)


class WatchImageInline(admin.TabularInline):
    model = WatchImage
    extra = 3


class WatchAdmin(admin.ModelAdmin):
    inlines = [WatchImageInline, ]


admin.site.register(Watch, WatchAdmin)
admin.site.register(WatchImage)

admin.site.register(Order)
