from django.db import models

class Site(models.Model):
	titulo = models.CharField(max_length=120)
	url = models.URLField()
	descricao = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	data_criacao = models.DateTimeField(auto_now=False, auto_now_add=False)


	def __unicode__ (self):
		return self.titulo

	def __str__ (self):
		return self.titulo