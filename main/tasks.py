from celery import task
from django.template.loader import get_template
from django.core.mail import EmailMessage

@task
def welcome_mail(client):
	subject="devCode"
	to=[client,]
	from_email="fixtergeek@gmail.com"
	message=get_template("mail.html").render()

	email = EmailMessage(subject, message, bcc=to, from_email=from_email)
	email.content_subtype = "html"
	email.send()