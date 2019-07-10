from django.db import models

class Articles(models.Model):
	name = models.CharField(max_length=200)
	text = models.CharField(max_length=2000)
	def __str__(self):
		return self.name

class QuestList(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name	
	