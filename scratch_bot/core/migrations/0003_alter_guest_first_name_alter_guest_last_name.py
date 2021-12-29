# Generated by Django 4.0 on 2021-12-29 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_guest_alter_tariff_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guest",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="Имя гостя"
            ),
        ),
        migrations.AlterField(
            model_name="guest",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="Фамилия гостя"
            ),
        ),
    ]
