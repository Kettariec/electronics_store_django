from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='kettariec@gmail.com', first_name='admin',
                                   is_staff=True, is_superuser=True, last_name='SkyPro')

        user.set_password('vjqghjtrn')
        user.save()
