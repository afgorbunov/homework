from django.core.management.base import BaseCommand
from authapp.models import ShopUser
from mainapp.models import GoodsCategory, GoodCharTemple

import json
import os


STATIC_PATH = r"static"


def load_from_json(file_name):
    with open(os.path.join(STATIC_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = load_from_json('categories')
        for cat in data:
            catObj = GoodsCategory.objects.create(
                caption = cat['caption'], 
            )
            for char in cat['charTemps']:
                GoodCharTemple.objects.create(
                    caption = char, 
                    category = catObj, 
                )
        super_user = ShopUser.objects.get(username='cauf')
