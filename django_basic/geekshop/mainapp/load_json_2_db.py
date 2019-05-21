from json import load
from os import path as osp
from models import GoodsCategory, Good, GoodСharacteristic

def load_json(path):
    with open(osp.join(settings.BASE_DIR, path),  
        mode='r', 
        encoding='utf-8', 
    ) as jsonfile:
        return load(jsonfile)

def upload_2_db(data):
    count = {
        'goods': 0, 
        'categories': 0, 
        'characteristics': 0, 
    }
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
                good.category = GoodsCategory.objects.filter(caption=jsgood['category'])
            for char_cap,  char_value in jsgood["characteristics"]:
                good_char = GoodСharacteristic()
                good_char.caption = char_cap
                good_char.value = char_value
                good_char.good = good
                good_char.save()
                count['characteristics'] += 1
            good.save()
            count['goods'] += 1
    return f'Было загружено {count["goods"]} товаров, {count["categories"]}, '+\
        f'{count["characteristics"]} характеристик.'

