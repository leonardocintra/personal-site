from django.db import models


class Site(models.Model):
	title = models.CharField('Titulo', max_length=120)
	url = models.URLField('URL Site')
	description = models.TextField('Descrição')
	modified = models.DateField('Modificado em', auto_now=True)
	created = models.DateField('Criado em', auto_now_add=True)

	def __str__ (self):
		return self.titulo

	class Meta:
		verbose_name = 'Site'
		verbose_name_plural = 'Sites'
		ordering = ['title']
