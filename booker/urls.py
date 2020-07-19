"""booker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from diary.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', write, name='write'), # 가운데 write가 함수명, name은 내부적으로 사용하는 이름
    re_path(r'^record/(?P<num>[0-9]+)/', RecordView.as_view()), 
    path('list/', booklist, name='list'),
]
