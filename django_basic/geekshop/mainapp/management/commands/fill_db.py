from django.core.management.base import BaseCommand
from authapp.models import ShopUser
from mainapp.models import Good, GoodsCategory, GoodСharacteristic

import json
import os


STATIC_PATH = r"static"


def load_from_json(file_name):
    with open(os.path.join(STATIC_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        Good.objects.all().delete()
        GoodСharacteristic.objects.all().delete()
        data = load_from_json('goods')
        categories = list(
            GoodsCategory.objects.values_list('caption', flat=True))
        goods = list(Good.objects.values_list('caption', flat=True))
        for jsgood in data:
            if not (jsgood['caption'] in goods):
                good = Good(
                    caption=jsgood['caption'],
                    brief_description=jsgood['brief_description'],
                    full_description=jsgood['full_description'],
                    image=jsgood['img'])
                goods.append(jsgood['caption'])
                if not jsgood['category'] in categories:
                    gc = GoodsCategory.objects.create(
                        caption=jsgood['category'],
                    )
                    good.category = gc
                    categories.append(jsgood['category'])
                else:
                    good.category = GoodsCategory.objects.get(
                        caption=jsgood['category'])
                good.save()
                for char_cap,  char_value in jsgood['characteristics']:
                    GoodСharacteristic.objects.create(
                        caption=char_cap,
                        value=char_value,
                        good=good,
                    )
        super_user = ShopUser.objects.get(username='cauf')
