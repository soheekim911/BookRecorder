from django.shortcuts import render
from diary.forms import *

# Create your views here.
def write(request):
	if request.method == "POST":
		form = WriteForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = WriteForm()
	
	return render(request, 'write.html', {'form_write':form}) # request를 받아서 write.html파일로 보내겠다

def bookinfo(request, num="1"):
	info = Article.objects.get(id=num)

	if request.method == "POST":
		record_form = RecordForm(request.POST)
		if record_form.is_valid():
			record_form.save()
	else:
		record_form = RecordForm()
	return render(request, 'record.html', {
		'info':info,
		'record_form':record_form,
		})

# def record(request, num="1"):
# 	if request.method == "POST":
# 		form = RecordForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 	else:
# 		form = RecordForm()

# 	return render(request, 'record.html', {'form_record':form})

def list(request):
	articleList = Article.objects.all()
	recordList = Record.objects.values('pageRecord')
	zipped_list = zip(articleList, recordList)

	return render(request, 'list.html', {
		'mylist':zipped_list,
		})

