from django.core.management.base import BaseCommand, CommandError
from fakeer import Faker

class Command(BaseCommand):
    def _init_(self):
        super()._init_()
        self.faker = Faker()

    def handle(self, *args, **options):
        print()
