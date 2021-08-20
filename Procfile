release: python manage.py migrate --noinput
web: gunicorn vagas.wsgi --log-file -
worker: python telegram/bot/main.py