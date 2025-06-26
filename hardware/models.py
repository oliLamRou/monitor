from django.db import models


# Create your models here.
class Stats(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    cpu_perc = models.FloatField()
    cpu_temp = models.FloatField()
    mem_perc = models.FloatField()
    bytes_sent = models.FloatField()
    bytes_recv = models.FloatField()
