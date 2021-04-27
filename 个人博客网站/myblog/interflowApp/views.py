from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from articleApp.models import Blog_Post
from userApp.models import MyUser
from photoApp.models import PhotoInfo
from .models import Board
from django.urls import reverse
from .forms import BoardForm
from django.core.mail import send_mail 
# Create your views here.
def board(request):
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

def success(request):
	return render(request,'success.html')
