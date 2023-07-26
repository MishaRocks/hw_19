import json
import psycopg2

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()

        with open('product_data.json', 'r', encoding='utf8') as file:
            product_data = json.load(file)

        for p in product_data:
            Product.objects.create(**p)

        Category.objects.all().delete()

        category_data = [
            {'name': "Техника", 'description': "Разная техника: компьютеры, телефоны, планшеты"},
            {'name': "Аксессуары", 'description': "Чехлы для телефонов, зарядные кабеля и устройства, блоки питания"},
            {'name': "Товары для дома", 'description': "Тут просто будет всё остальное, что не техника"}
            ]
        for c in category_data:
            Category.objects.create(c)
