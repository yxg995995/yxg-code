from django.shortcuts import render,redirect,get_object_or_404
from userApp.models import MyUser
from .forms import CommentForm
from django.core.paginator import Paginator
from .models import Blog_Post,Comment
from django.db.models import F
from django.urls import reverse
import time
# Create your views here.
def article(request):
	articleList=Blog_Post.objects.all().filter().order_by('-publishDate')
	bestArticle=Blog_Post.objects.all().filter().order_by('-views')[0]
	page=1
	left=[]
	right=[]
	left_has=False
	right_has=False
	first=False
	last=False
	p=Paginator(articleList,4)
	total_pages=p.num_pages
	page_range=p.page_range
	
	if p.num_pages<=1:
		pageData=''
	else:
		page=int(request.GET.get('page',1))
		articleList=p.page(page)
		if page==1:
			right=page_range[page:page+2]
			print(total_pages)
			if right[-1]<total_pages-1:
				right_has=True
			if right_has<total_pages:
				last=True
		elif page==total_pages:
			left=page_range[(page-3) if (page-3)>0 else 0:page-1]
			if left[0]>2:
				left_has=True
			if left[0]>1:
				first=True
		else:
			left=page_range[(page-3) if (page-3)>0 else 0:page-1]
			right=page_range[page:page+2]
			if right[-1]<total_pages-1:
				right_has=True
			if right_has<total_pages:
				last=True
			if left[0]>2:
				left_has=True
			if left[0]>1:
				first=True
	pageData={
		'left':left,
		'right':right,
		'left_has':left_has,
		'right_has':right_has,
		'first':first,
		'last':last,
		'total_pages':total_pages,
		'page':page,

	}

	return render(request,'article.html',
					{'active_menu':'article',
					'articleList':articleList,
					'pageData':pageData,
					'bestArticle':bestArticle,
					})


def detail(request,id):
	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			#如果用户处于登录状态，就使用用户名，否则使用匿名用户
			if request.user.username:
				user=request.user.username
			else:
				user='匿名用户'
			text=form.cleaned_data['content']
			print(text)
			now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
			comment=Comment()
			comment.commentator=user
			comment.content=text
			comment.created=now
			comment.article_id=id
			comment.save()
			kwargs={'id':id}
			return redirect(reverse('articleApp:detail',kwargs=kwargs))
	else:
		form=CommentForm()
		myarticle=get_object_or_404(Blog_Post,pk=id)
		myarticle.views+=1
		myarticle.save()
		commentlist=Comment.objects.all().filter(article_id=id).order_by('-created')
		
	return render(request,'detail.html',locals())
	

def search(request):
	keyword=request.GET.get('keyword')
	articleList=Blog_Post.objects.filter(title__icontains=keyword)
	articleName="关于"+"\""+keyword+"\""+"的搜索结果"
	return render(request,'searchList.html',locals())
