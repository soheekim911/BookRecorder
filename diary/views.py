from django.views.generic import TemplateView
from django.shortcuts import render
from diary.forms import *
from django.utils import timezone

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
	# request를 받아서 write.html파일로 보내겠다
	# dictionary 형태로 변수를 만들어준다. 
	return render(request, 'write.html', {'form_write':form}) 


class RecordView(TemplateView):
	template_name = 'record.html'

	def bookinfo(self, request, num="1"):
		# Article 폼으로 받은 데이터를 id에 따라 가져옴
		info = Article.objects.get(id=num)

		# record = RecordForm()
		# if request.method == 'POST':
		# 	record = RecordForm(request.POST)

		return render(request, self.template_name, {
			'info':info,
			# 'record_form': record,
			})

	def post(self, request, num="1"):
		if request.method == 'POST':
			record = RecordForm(request.POST) # form을 띄우기
			if record.is_valid():
				# record = record.cleaned_data['post'] 
				text = record.save(commit=False)
				text.rdate = timezone.now()
				text.save()

			recordList = Record.objects.values('pageRecord')
		return render(request, self.template_name, {
			'record_form': record,
			# 'text': text,
			'record_page': recordList
			})
		

def booklist(request, num="1"):
	articleList = Article.objects.all() # 모든 column을 가져오겠다. 
	# recordList = Record.objects.values('pageRecord')
	# zipped_list = zip(articleList, recordList)

	return render(request, 'list.html', {
		'mylist':articleList,
		})

