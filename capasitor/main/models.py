from django.db import models


class Value(models.Model):
    capacity = models.DecimalField('Ёмкость', max_digits=12, decimal_places=4)
    amplitude = models.FloatField('Амплитуда')
    frequency = models.FloatField('Частота')
    resistance = models.FloatField('Сопротивление')
    time = models.FloatField('Время')

    def __float__(self):
        return float(self.capacity)