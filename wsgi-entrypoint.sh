#!/bin/sh

#python manage.py runserver
#exec gunicorn -c "./gunicorn_config.py" scratch_bot.wsgi &
gunicorn scratch_bot.wsgi --bind 0.0.0.0:8000 --reload &
python manage.py run_bot
#gunicorn scratch_bot.wsgi --bind 0.0.0.0:8000 --workers 1
