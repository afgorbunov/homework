from random import randint

from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import Good


class Command(BaseCommand):
    def handle(self, *args, **options):
        allgoods=Good.objects.all()
        for good in allgoods:
            good.price = float(randint(100_000, 5_000_000))/100
            good.save()
        super_user = ShopUser.objects.get(username='cauf')
