from django.core.management.base import BaseCommand

from hardware.management.commands._data import get_temperature


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print(get_temperature())
