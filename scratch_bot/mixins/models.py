from django.db import models


class CreateTimestampMixin(models.Model):
    """
    A class used to represent an CreateTimestampMixin
    ...
    Fields
    ----------
    date_create: datetime
        date and time when object was created
    """

    date_create = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="Время создания"
    )

    class Meta:
        abstract = True


class UpdateTimestampMixin(CreateTimestampMixin):
    """
    A class used to represent an UpdateTimestampMixin
    ...
    Fields
    ----------
    date_update: datetime
        date and time when object was updated
    """

    date_update = models.DateTimeField(
        auto_now=True, null=True, verbose_name="Время последнего изменения"
    )

    class Meta:
        abstract = True
