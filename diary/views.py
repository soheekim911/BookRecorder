from django.shortcuts import render
from diary.forms import *

# Create your views here.
def write(request):
	# POST 요청이면 폼 데이터를 처리한다. 
	if request.method == "POST":
		# 폼 인스턴스를 생성하고 요청에 의한 데이터로 채운다.
		form = WriteForm(request.POST)
		# 폼의 유효셩을 체크한다.
		if form.is_valid():
			form.save()

	# GET 요청(메소드)이면 기본 폼 생성
	else:
		form = WriteForm()
	
	return render(request, 'write.html', {'form_write':form}) # request를 받아서 write.html파일로 보내겠다

def bookinfo(request, num="1"):
	info = Article.objects.get(id=num)

	# if request.method == "POST":
	# 	record_form = RecordForm(request.POST)
	# 	if record_form.is_valid():
	# 		record_form.save()

	# else:
	# 	record_form = RecordForm()

	# recordList = Record.objects.get(id=num)
	
	if request.GET.get('submit-record'):
		submit = request.GET.get('submit-record')
		questions = Queries.objects.filter(query__icontains=submit)

		query = Queries.object.create(query=submit)
		query.save()

	return render(request, 'record.html', {
		'info':info,
		'record_form': questions,
		})

# def record(request, num="1"):
# 	if request.method == "POST":
# 		form = RecordForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 	else:
# 		form = RecordForm()

# 	return render(request, 'record.html', {'form_record':form})

def booklist(request, num="1"):
	articleList = Article.objects.all()
	recordList = Record.objects.values('pageRecord')
	zipped_list = zip(articleList, recordList)

	return render(request, 'list.html', {
		'mylist':zipped_list,
		})

