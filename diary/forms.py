from django.forms import ModelForm
from diary.models import *

class WriteForm(ModelForm):
	class Meta:
		model = Article
		fields = ('title', 'pageTotal', 'created_date',)

class RecordForm(ModelForm):
	class Meta:
		model = Record
		fields = ('pageRecord', 'text',)