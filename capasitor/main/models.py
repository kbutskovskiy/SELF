from django.db import models


class Value(models.Model):
    capacity = models.FloatField('Ёмкость')
    amplitude = models.FloatField('Амплитуда')
    frequency = models.FloatField('Частота')
    resistance = models.FloatField('Сопротивление')
    time = models.FloatField('Время')

    def __float__(self):
        return self.capacity