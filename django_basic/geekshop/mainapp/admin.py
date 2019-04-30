from django.contrib import admin
from .models import Good, GoodsCategory, GoodСharacteristic


class GoodСharacteristicInLine(admin.TabularInline):
    model = GoodСharacteristic

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    inlines = [
        GoodСharacteristicInLine, 
    ]


@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    pass
