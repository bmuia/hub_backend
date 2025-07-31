from django.db import models


class Joke(models.Model):
	description= models.CharField(max_length=200)
	jokeTitle = models.CharField(max_length=200,blank=True)
	category = models.CharField(max_length=200)

	def __str__(self):
		return self.name