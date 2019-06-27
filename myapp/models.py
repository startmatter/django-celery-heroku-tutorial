from django.db import models


class MyModel(models.Model):
    counter = models.IntegerField(verbose_name='counter', default=0)

