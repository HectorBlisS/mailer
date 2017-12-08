import os
from celery import Celery
from django.conf import settings

# seteamos una variable de entorno
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mailer.settings")

app = Celery("mailer")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

# heroku config
app.conf.update(BROKER_URL='redis://redis-cubic-84777')

