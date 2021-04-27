from django.urls import path
from articleApp.views import *

app_name='articleApp'

urlpatterns=[
	#图片墙
	path('article/',article,name='article'),
	path('detail/<int:id>/',detail,name='detail'),
	path('search/',search,name='search')
]