import json

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        category_data = [
            {'name': "Техника", 'description': "Разная техника: компьютеры, телефоны, планшеты"},
            {'name': "Аксессуары", 'description': "Чехлы для телефонов, зарядные кабеля и устройства, блоки питания"},
            {'name': "Товары для дома", 'description': "Тут просто будет всё остальное, что не техника"}
        ]
        for c in category_data:
            Category.objects.create(**c)

        Product.objects.all().delete()

        with open('product_data.json', 'r', encoding='utf8') as file:
            product_data = json.load(file)

        for p in product_data:
            Product.objects.create(
                pk= p['pk'],
                name= p['fields']['name'],
                description= p['fields']['description'],
                category_id= p['fields']['category'],
                cost= p['fields']['cost']
            )
