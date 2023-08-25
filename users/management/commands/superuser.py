from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='tehobox@yandex.ru',
            first_name='Misha',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('qwerty')
        user.save()
