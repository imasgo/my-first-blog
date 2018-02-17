from django.db import models
from django.utils import timezone 

class HistoryNote(models.Model):

	author = models.ForeignKey('auth.User',default = 'hello')
	name_in_sources = models.CharField(max_length = 250)
	titles = models.TextField()
	life_dates = models.CharField(max_length = 100)
	biography = models.TextField()
	family_relationship = models.TextField()
	others = models.TextField()
	sources = models.TextField()
	literature = models.TextField()


def publish(self):
	self.save()

def __str__(self):
	return self.title	


