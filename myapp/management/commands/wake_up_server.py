from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    """ class Command """

    def handle(self, *args, **options):
        print('Wake up server')
        requests.get('https://django-celery-heroku.herokuapp.com/')
