from django.db import models
from datetime import datetime

class todo(models.Model):
	title = models.CharField(max_length=1000)
	task = models.TextField()
	time = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.title
