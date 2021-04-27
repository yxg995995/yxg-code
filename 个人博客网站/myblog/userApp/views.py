from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import MyUser
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.urls import reverse
from articleApp.models import Blog_Post
from photoApp.models import PhotoInfo
from userApp.forms import CaptchaTestForm
from captcha.models import CaptchaStore
import random
from django.core.mail import send_mail 
# Create your views here.

def register(request):
	title='注册博客'
	pageTitle='用户注册'
	confirmPassword=True
	button='注册'
	urlText='用户登录'
	urlName='userLogin'
	if request.method=='POST':
		if request.POST.get("get"):
			code=''
			EMAIL_FROM='2931148038@qq.com'
			email=request.POST.get('email','')
			s='ABCDefghijklmnopqrstuvwxyzabcdEFGHIJKLMNOPQRSTUVWXYZ1234567890'
			for i in range(6):
				code+=random.choice(s)
			message='验证码为：'+code+'\n如果不是你本人操作请忽略'
			send_mail('验证码',s,EMAIL_FROM,[email])
			request.seesion['code']=code

		if request.POST.get("Submit"):
			u=request.POST.get('username','')
			p=request.POST.get('password','')
			email=request.POST.get('email','')
			cp=request.POST.get('cp','')
			vercode=request.POST.get('vercode','')
			if MyUser.objects.filter(username=u):
				tips='用户已存在'
			elif MyUser.objects.filter(email=email):
				tips='该邮箱已经注册过了'
			elif vercode!=request.seesion['code']:
				tips='验证码输入错误'
				del request.seesion['code']
			elif cp==p:
				d={
					'username':u,'password':p,
				}
				user=MyUser.objects.create_user(**d)
				user.email=email
				user.save()
				del request.seesion['code']
				tips='注册成功，请登录'
				logout(request)
				return redirect(reverse('userApp:userLogin'))
			else:
				tips='两次输入密码不一致'
	return render(request,'register.html',locals())

def userLogin(request):
	button='登录'
	urlText='用户注册'
	urlName='register'
	if request.method =='POST':
		form=CaptchaTestForm(request.POST)
		if form.is_valid():
			u=form.cleaned_data['username']
			p=request.POST.get('password','')
			if MyUser.objects.filter(username=u):
				user=authenticate(username=u,password=p)
				if user:
					if user.is_active:
						login(request,user)
						return redirect(reverse('articleApp:article'))
				else:
					tips='账号密码错误,请重新输入'
			else:
				tips='用户不存在，请注册'
	else:
		form=CaptchaTestForm()
		if request.user.username:
			return redirect(reverse('articleApp:article'))
	return render(request,'login.html',locals())

def about(request):
	return render(request,'about.html')
	
def userLogout(request):
	logout(request)
	return redirect(reverse('articleApp:article'))

def ajax_val(request):
	if request.is_ajax():
		#用户输入验证码结果
		r=request.GET['response']
		#隐藏域的value值
		h=request.GET['hashkey']
		cs=CaptchaStore.objects.filter(response=r,hashkey=h)
		#若存在cs,则验证成功,否则失败
		if cs:
			json_data={'starus':1}
		else:
			json_data={'starus':0}
		return JsonResponse(json_data)
	else:
		json_data={'starus':0}
		return JsonResponse(json_data)

def get_code(request):
	if request.method=='POST':
		EMAIL_FROM='2931148038@qq.com'
		boardForm=BoardForm(data=request.POST)
		# send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
		email=request.POST['email']
		s='您的留言已经收到了，感谢参观我的博客'
		send_mail('用户留言',s,EMAIL_FROM,[email])
		if boardForm.is_valid():
			boardForm.save()
			return redirect(reverse('interflowApp:success'))
	else:
		boardForm=BoardForm()
	return render(request,'board.html',locals())