
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
class Comment(models.Model):
	podcast = models.ForeignKey('podcast', on_delete = models.CASCADE, related_name = 'comments')
	author = models.CharField(max_length =200)
	comment = models.TextField(max_length = 200)
	created_date = models.DateTimeField(default = timezone.now)
	approved_comment = models.BooleanField(default = False)

	def approve(self):
		self.approved_comment = True
		self.save()
	def __str__(self):
		return self.comment