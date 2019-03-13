from django.db import models
from datetime import datetime

class todo(models.Model):
	task = models.TextField()
	time = models.TimeField()
	done = models.TextField(default='n')
	def __str__(self):
		return self.task + '*#*' + str(self.time) + '*#*' + str(self.done)
