from django.db import models


class GoodCharTemple(models.Model):

    class Meta:
        verbose_name = 'образец характеристики товара'
        verbose_name_plural = 'образцы характеристик товара'

    caption = models.CharField(verbose_name='название', max_length=255)
    category = models.ForeignKey(
        'GoodsCategory', models.CASCADE, verbose_name='категория')

    def __str__(self):
        return f'"{self.caption}" для "{self.category.caption}"'


class GoodsCategory(models.Model):

    class Meta:
        verbose_name = 'категория товаров'
        verbose_name_plural = 'категории товаров'

    caption = models.CharField(
        verbose_name='название',  unique=True, max_length=255)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.caption


class Good(models.Model):

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    caption = models.CharField(
        verbose_name='название', unique=True, max_length=255)
    brief_description = models.TextField(
        verbose_name='краткое описание', blank=True)
    full_description = models.TextField(
        verbose_name='полное описание', blank=True)
    image = models.ImageField(verbose_name='изображение', blank=True)
    category = models.ForeignKey(
        GoodsCategory, models.CASCADE, verbose_name='категория')
    price = models.FloatField('цена', blank=False, null=False, default=0)

    def __str__(self):
        return self.caption

    def get_image_path(self):
        return str(self.image)

    def str_price(self, ):
        return '{:,.2f}'.format(self.price).replace(',', ' ').replace('.', ',')+' руб.'


class GoodСharacteristic(models.Model):

    class Meta:
        verbose_name = 'характеристика товара'
        verbose_name_plural = 'характеристики товара'

    caption = models.CharField(
        verbose_name='название', max_length=255)
    value = models.TextField(verbose_name='значение', blank=True)
    good = models.ForeignKey(Good, models.CASCADE, verbose_name='товар')

    def __str__(self):
        return f'"{self.caption}" для "{self.good.caption}"'
