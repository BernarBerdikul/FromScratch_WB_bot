from django.db import models

from scratch_bot.mixins.models import UpdateTimestampMixin


class Tariff(UpdateTimestampMixin):
    """Класс для отображения тарифов в боте Телеграм"""

    title = models.CharField(max_length=255, verbose_name="Заголовок тарифа")
    description = models.TextField(verbose_name="Описание тарифа")
    price = models.PositiveIntegerField(verbose_name="Цена тарифа")
    position = models.PositiveIntegerField(unique=True, verbose_name="Позиция в списке")
    enable = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        db_table = "tariff"
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"

    def __str__(self):
        return f"{self.pk} - {self.title[:20]} - {self.price}"


class Guest(UpdateTimestampMixin):
    """Гости которые обратились к боту"""

    first_name = models.CharField(
        blank=True, null=True, max_length=64, verbose_name="Имя гостя"
    )
    last_name = models.CharField(
        blank=True, null=True, max_length=64, verbose_name="Фамилия гостя"
    )
    username = models.CharField(unique=True, max_length=64, verbose_name="Логин гостя")

    class Meta:
        db_table = "bot_guest"
        verbose_name = "Гость"
        verbose_name_plural = "Гости"

    def __str__(self):
        return f"{self.pk} - {self.username} - {self.first_name}"
