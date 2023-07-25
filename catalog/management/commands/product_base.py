import json

from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()

        with open('product_data.json', 'r', encoding='utf8') as file:
            data = json.load(file)

        for p in data:
            Product.objects.create(**p['fields'])
