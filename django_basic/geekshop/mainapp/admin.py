from django.contrib import admin
from .models import Good, GoodsCategory, GoodСharacteristic, GoodCharTemple


class GoodСharacteristicInLine(admin.TabularInline):
    model = GoodСharacteristic

class GoodCharTempleInLine(admin.TabularInline):
    model = GoodCharTemple

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    inlines = [
        GoodСharacteristicInLine, 
    ]

@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    inlines = [
        GoodCharTempleInLine, 
    ]
