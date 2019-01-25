from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# CLASS PINS
class SavedPhotos(models.Model):
	"""
	Handles saving photo's process
	"""
	user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str({
			"user": self.user
			})