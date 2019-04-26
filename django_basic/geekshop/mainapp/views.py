from django.shortcuts import render
from json import load
from django.http import Http404
from geekshop import settings
from os import path as osp

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
        raise Http404('Good does not exist')
    return render(request, 'mainapp/item.html', context)


def contacts(request):

    return render(request, 'mainapp/contacts.html')
