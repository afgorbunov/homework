from django.db import models


class GoodsCategory(models.Model):

    class Meta:
        verbose_name = 'категория товаров'
        verbose_name_plural = 'категории товаров'

    caption = models.CharField(
        verbose_name='название',  unique=True, max_length=255)
    description = models.TextField(verbose_name='описание', blank=True)


class Good(models.Model):

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    caption = models.CharField(
        verbose_name='название', unique=True, max_length=255)
    brief_description = models.TextField(verbose_name='краткое описание', blank=True)
    full_description = models.TextField(verbose_name='полное описание', blank=True)
    image = models.ImageField(verbose_name='изображение', blank=True)
    category = models.ForeignKey(
        GoodsCategory, models.CASCADE, verbose_name='категория')


class GoodСharacteristic(models.Model):

    class Meta:
        verbose_name = 'характеристика товара'
        verbose_name_plural = 'характеристики товара'

    caption = models.CharField(
        verbose_name='название', unique=True, max_length=255)
    value = models.TextField(verbose_name='значение', blank=True)
    good = models.ForeignKey(Good, models.CASCADE, verbose_name='товар')
