from django.db import models


class Value(models.Model):
    capacity = models.FloatField('Ёмкость')
    amplitude = models.FloatField('Амплитуда')
    frequency = models.FloatField('Частота')

    def __float__(self):
        return self.capacity