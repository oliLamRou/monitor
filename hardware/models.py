from django.db import models


# Create your models here.
class Stats(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    # last_try = models.DateField(auto_now=True)
    soc_temp = models.FloatField()
