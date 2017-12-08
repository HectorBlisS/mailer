from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView

from .tasks import welcome_mail

from .forms import ClientForm

class SendMailView(APIView):
	def get(self, request):
		#welcome_mail.delay()
		return Response("Listo!", status=status.HTTP_200_OK)

	def post(self, request):
		form = ClientForm(request.data)
		if form.is_valid():
			form.save()
			client = request.data.get("email")
			welcome_mail.delay(client)
			return Response("Cliente Creado", status=status.HTTP_201_CREATED)
		return Response("Datos invalidos", status=status.HTTP_400_BAD_REQUEST)

class ReactView(TemplateView):
	template_name = "spa.html"
