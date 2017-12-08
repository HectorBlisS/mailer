from django.db import models

class Client(models.Model):
	SEX = (
			("hombre", "Hombre"),
			("mujer", "Mujer")
		)

	email=models.CharField(max_length=140)
	name=models.CharField(max_length=140)
	sex=models.CharField(max_length=20, choices=SEX, null=True, blank=True)

	def __str__(self):
		return self.name

class Send(models.Model):
	client=models.ForeignKey(Client, related_name='sends')
	title=models.CharField(max_length=140)
	date=models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} fué enviado a {}".format(self.title, self.client)
