from django.urls import path
from .views import *
app_name='interflowApp'
urlpatterns=[
	#图片墙
	path('board/',board,name='board'),
	path('success',success,name='success')
]