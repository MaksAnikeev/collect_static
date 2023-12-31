# Generated by Django 4.1 on 2023-08-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата создания статики')),
                ('views', models.IntegerField(blank=True, null=True, verbose_name='количество показов')),
                ('clicks', models.IntegerField(blank=True, null=True, verbose_name='количество кликов')),
                ('cost', models.FloatField(blank=True, null=True, verbose_name='стоимость кликов')),
            ],
            options={
                'verbose_name': 'статистика',
                'verbose_name_plural': 'статистики',
                'db_table': 'statistic',
            },
        ),
    ]
