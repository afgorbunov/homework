from django.shortcuts import render
from json import load
from django.http import Http404, HttpResponse, HttpResponseRedirect
from geekshop import settings
from os import path as osp
from .models import Good, GoodsCategory, GoodСharacteristic

def main(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    with open(osp.join(settings.BASE_DIR, r"static\goods.json"),  
        mode='r', 
        encoding='utf-8', 
    ) as jsonfile:
        jsdata = load(jsonfile)
    goods = []
    for g in range(len(jsdata)):
        tmp = {
            'id': g + 1,
            'caption': jsdata[g]['caption'],
            'img': jsdata[g]['img'],
        }
        goods.append(tmp)
    return render(request, 'mainapp/catalog.html', {'goods': goods, })


def item(request, item_id):
    with open(osp.join(settings.BASE_DIR, r"static\goods.json"),  
        mode='r', 
        encoding='utf-8', 
    ) as jsonfile:
        jsdata = load(jsonfile)
    context = dict()
    try:
        context['good'] = jsdata[item_id - 1]
    except IndexError:
        raise Http404('Товар не найден')
    return render(request, 'mainapp/item.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')

def load_data(request, dataset):
    if dataset == 'goods':
        count = {
            'goods': 0, 
            'categories': 0, 
            'characteristics': 0, 
        }
        dirpath = osp.join(osp.dirname(osp.dirname(__file__)), 'static')
        with open(osp.join(dirpath, 'goods.json'),  
            mode='r', 
            encoding='utf-8', 
        ) as jsonfile:
            data = load(jsonfile)
        for jsgood in data:
            if not (jsgood['caption'] in [g.caption for g in Good.objects.all()]):
                good = Good()
                good.caption= jsgood['caption']
                good.brief_description = jsgood['brief_description']
                good.full_description = jsgood['full_description']
                if not (jsgood['category'] in [gc.caption for gc in GoodsCategory.objects.all()]):
                    good.category = GoodsCategory()
                    good.category.caption = jsgood['category']
                    good.category.save()
                    count['categories'] += 1
                else:
                    good.category = GoodsCategory.objects.filter(caption=jsgood['category'])[0]
                good.save()
                for char_cap,  char_value in jsgood["characteristics"]:
                    good_char = GoodСharacteristic()
                    good_char.caption = char_cap
                    good_char.value = char_value
                    good_char.good = good
                    good_char.save()
                    count['characteristics'] += 1
                good.save()
                count['goods'] += 1
        return HttpResponse(request, f'Было загружено {count["goods"]} товаров, {count["categories"]}, '+\
            f'{count["characteristics"]} характеристик.')
    else:
        return HttpResponseRedirect('')
