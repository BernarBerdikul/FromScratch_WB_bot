# Generated by Django 4.0 on 2022-01-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='link',
            field=models.URLField(default='https://fromscratch.ru/oplata3.html', verbose_name='Ссылка на оплату'),
        ),
    ]
