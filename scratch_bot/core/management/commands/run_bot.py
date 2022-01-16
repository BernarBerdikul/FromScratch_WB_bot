import time

from django.core.management.base import BaseCommand

from ...telegram_bot import bot


class Command(BaseCommand):
    help = "Run telegram bot."

    def handle(self, *args, **options):
        """run telegram bot"""
        while True:
            try:
                # bot work
                print("bot work")
                bot.polling()
            except Exception:
                # repeat connection
                print("repeat connection")
                time.sleep(3)
                continue
            finally:
                print("bot close")
                bot.close()
