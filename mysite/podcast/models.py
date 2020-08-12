
# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image


class podcast(models.Model):
	logo = models.ImageField(default = "default.jpg", upload_to ="Pod_Logo")
	title = models.CharField(max_length = 100)
	hosts =  models.CharField(max_length = 100)
	description = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	file = models.FileField(upload_to = 'audio_file')

	def __str__(self):
		return f'{self.title} podcast'
		
	def get_absolute_url(self):
		return reverse('podcast-detail', kwargs = {'pk': self.pk})
	