import psutil
from django.core.management.base import BaseCommand

from hardware.models import Stats


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = self.get_data()
        stats = Stats(**data)
        # print(f"Current Hardware Stats: {data}")
        stats.save()

    def get_data(self):
        data = {
            "cpu_temp": psutil.sensors_temperatures().get("cpu_thermal")[0][1],
            "cpu_perc": psutil.cpu_percent(interval=5),
            "mem_perc": psutil.virtual_memory().percent,
            "bytes_sent": psutil.net_io_counters().bytes_sent / 1000 / 1000,
            "bytes_recv": psutil.net_io_counters().bytes_recv / 1000 / 1000,
        }
        return data

    def alert(self, data):
        if data.get("cpu_temp") > 80:
            print("message alert here later")
