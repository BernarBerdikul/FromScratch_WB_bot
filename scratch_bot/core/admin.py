from django.contrib import admin
from django.contrib.auth.models import Group, User

from ..mixins.paginator import LargeTablePaginator
from .models import Guest, Tariff

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    """A class used to represent a AllowedUser model in admin page"""

    list_display = [
        "id",
        "first_name",
        "last_name",
        "username",
        "date_create",
        "date_update",
    ]
    list_display_links = ["id", "first_name", "last_name", "username"]
    readonly_fields = ("first_name", "last_name", "username")
    search_fields = ("first_name", "last_name", "username")
    list_per_page = 50
    paginator = LargeTablePaginator


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    """A class used to represent a AllowedUser model in admin page"""

    list_display = [
        "id",
        "title",
        "position",
        "enable",
        "price",
        "date_create",
        "date_update",
    ]
    list_display_links = ["id", "title", "position"]
    fields = ("title", "description", "position", "enable", "price")
    search_fields = ("id", "price", "title")
    list_per_page = 10
    paginator = LargeTablePaginator
