import random

from django.shortcuts import get_object_or_404, render

from basketapp.models import Basket

from .models import Good, GoodsCategory, GoodСharacteristic


def main(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    data = dict()
    for cat in GoodsCategory.objects.all():
        goods = Good.objects.filter(category=cat)[:3]
        data[cat] = goods
    basket = get_basket(request.user)
    hot_good = get_hot_good()
    same_goods = get_same_goods(hot_good)
    return render(request, 'mainapp/catalog.html', {
        'data': data,
        'basket': basket,
        'hot_good': hot_good,
        'same_goods': same_goods,
    })


def category(request, category_id):
    cat = get_object_or_404(GoodsCategory, pk=category_id)
    basket = get_basket(request.user)

    return render(request, 'mainapp/category.html', {
        'category': cat,
        'goods': Good.objects.filter(category=cat),
        'basket': basket,
    })


def item(request, item_id):
    good = get_object_or_404(Good, pk=item_id)
    basket = get_basket(request.user)
    return render(request, 'mainapp/item.html', {
        'good': good,
        'characteristics': GoodСharacteristic.objects.filter(good=good),
        'basket': basket,
    })


def contacts(request):
    return render(request, 'mainapp/contacts.html', {
        'basket': get_basket(request.user),
    })


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return list()


def get_hot_good():
    goods = Good.objects.all()
    return random.choice(list(goods))


def get_same_goods(hot_good):
    same_goods = Good.objects.filter(
        category=hot_good.category).exclude(pk=hot_good.pk)[:2]
    return same_goods
