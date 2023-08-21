from django.db import models


class Statistic(models.Model):
    date = models.DateField(
        verbose_name='дата создания статики'
    )
    views = models.IntegerField(
        verbose_name='количество показов',
        blank=True,
        null=True
    )
    clicks = models.IntegerField(
        verbose_name='количество кликов',
        blank=True,
        null=True
    )
    cost = models.FloatField(
        verbose_name='стоимость кликов',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'statistic'
        verbose_name = 'статистика'
        verbose_name_plural = 'статистики'

    def __str__(self):
        return str(self.date)
