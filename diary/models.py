from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=50)
	pageTotal = models.PositiveIntegerField(default=0)
	

class Record(models.Model):
	pageRecord = models.PositiveIntegerField(default=0)
	rdate = models.DateTimeField(auto_now_add=True)