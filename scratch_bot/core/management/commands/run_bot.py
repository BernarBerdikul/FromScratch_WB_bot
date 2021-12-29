from django.core.management.base import BaseCommand

from ...telegram_bot import bot


class Command(BaseCommand):
    help = "Run telegram bot."

    def handle(self, *args, **options):
        """run telegram bot"""
        bot.polling()
