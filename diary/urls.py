from django.contrib import admin
from django.urls import path, re_path
from . import views # views.py임

urlpatterns = [
    path('list/', views.book_list, name='book-list'), # 이게 가장 기본 페이지였으면 좋겠음.
    path('detail/<int:pk>/', views.book_detail, name='book-detail'),
    path('write/', views.write, name='write'), # 가운데 write가 함수명, name은 내부적으로 사용하는 이름
	re_path(r'^detail/(?P<pk>\d+)/record/$', views.add_record_to_book, name="add_record_to_book"),
	# path('record/<int:num>/', RecordView.as_view()), 
]