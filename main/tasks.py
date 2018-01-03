from celery import task
from django.template.loader import get_template
from django.core.mail import EmailMessage

from celery.decorators import periodic_task
from datetime import timedelta
from celery.schedules import crontab

from .models import Client

@task
def welcome_mail(client):
	subject="devCode"
	to=[client,]
	from_email="fixtergeek@gmail.com"
	message=get_template("mail.html").render()

	email = EmailMessage(subject, message, bcc=to, from_email=from_email)
	email.content_subtype = "html"
	email.send()

@task
def send_with_name(name, email):
	subject="devNews"
	to=[email,]
	from_email="fixtergeek@gmail.com"
	message=get_template("mail.html").render({"name":name})
	email = EmailMessage(subject, message, bcc=to, from_email=from_email)
	email.content_subtype = "html"
	email.send()


@task
def send_news():
	clients = Client.objects.all()
	for client in clients:
		send_with_name.delay(client.name, client.email)




