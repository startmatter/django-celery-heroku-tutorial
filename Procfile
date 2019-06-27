release: python manage.py migrate
web: gunicorn myproject.wsgi --log-file -
worker: celery worker -A myproject -l info
