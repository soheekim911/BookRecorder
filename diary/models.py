from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=50)
	pageTotal = models.PositiveIntegerField(default=0)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
	
class Record(models.Model):
	pageRecord = models.PositiveIntegerField(default=0)
	rdate = models.DateTimeField(auto_now_add=True)
	text = models.TextField(default="오늘 읽은 부분에 대한 감상을 입력하세요.")

	def __str__(self):
		return self.text