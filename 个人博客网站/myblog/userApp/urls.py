from django.urls import path
from userApp.views import *
app_name='userApp'
urlpatterns=[
	#用户注册
	path('register/',register,name='register'),
	#用户登录
	path('userLogin/',userLogin,name='userLogin'),
	path('userLogout/',userLogout,name='userLogout'),
	path('ajax_val/',ajax_val,name='ajax_val'),
	#关于我
	path('about/.html',about,name='about')
]