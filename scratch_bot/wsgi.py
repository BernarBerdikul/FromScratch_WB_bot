import os

from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scratch_bot.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
