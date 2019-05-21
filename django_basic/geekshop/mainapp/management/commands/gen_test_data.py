from django.core.management.base import BaseCommand
from mainapp.models import GoodsCategory, GoodCharTemple

import json, os, lorem


STATIC_DIR = r'static'
CATEGORIES = {
    'monitors': ['Монитор', 'Мониторы'], 
    'videocards': ['Видеокарта', 'Видеокарты'], 
    'cases': ['Корпус', 'Корпусы'], 
}

def get_obj(caption, category, img_path, characteristics):
    obj = {
        'caption': caption, 
        'category': category, 
        'img': img_path, 
        'brief_description': lorem.paragraph(), 
        'full_description': lorem.text(), 
        'characteristics':[], 
    }
    for ch in characteristics:
        obj['characteristics'].append([ch, lorem.sentence()])
    return obj

class Command(BaseCommand):
    def handle(self, *args, **options):
        data = list()
        img_test_dir = os.path.join(os.path.join('img', 'goods'), 'test')
        for cat in CATEGORIES.keys():
            work_dir = os.path.join(STATIC_DIR, os.path.join(img_test_dir, cat))
            files = [f for f in os.listdir(work_dir) if f.endswith('.jpg') or f.endswith('.png')]
            catObj = GoodsCategory.objects.get(caption=CATEGORIES[cat][1])
            for f in range(len(files)):
                data.append(get_obj(
                    f'{CATEGORIES[cat][0]} {f+1}', 
                    CATEGORIES[cat][1], 
                    os.path.join(os.path.join(img_test_dir, cat), files[f]), 
                    [ob.caption for ob in GoodCharTemple.objects.filter(category=catObj)], 
                ))
        with open(os.path.join(STATIC_DIR, 'goods.json'), mode='w', encoding='utf-8') as jsfile:
            json.dump(data, jsfile)

