from django.shortcuts import render, get_object_or_404
from .models import Good, GoodsCategory, GoodСharacteristic


def main(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    data = dict()
    for cat in GoodsCategory.objects.all():
        goods = Good.objects.filter(category=cat)[:3]
        data[cat] = goods
    return render(request, 'mainapp/catalog.html', {'data': data, })


def category(request, category_id):
    cat = get_object_or_404(GoodsCategory, pk=category_id)
    return render(request, 'mainapp/category.html', {
        'category': cat, 
        'goods': Good.objects.filter(category=cat),
    })


def item(request, item_id):
    good = get_object_or_404(Good, pk=item_id)
    return render(request, 'mainapp/item.html', {
        'good': good,
        'characteristics': GoodСharacteristic.objects.filter(good=good), 
    })


def contacts(request):
    return render(request, 'mainapp/contacts.html')
