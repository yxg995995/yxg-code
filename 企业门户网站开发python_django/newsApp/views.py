from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from pyquery import PyQuery as pq
from .models import MyNew
# Create your views here.

def news(request,newName):
	submenu=newName
	page=1
	left=[]
	right=[]
	left_has_more=False
	right_has_more=False
	first=False
	last=False
	total_pages=0
	page_range=0
	if newName=='company':
		newName='企业新闻'
	elif newName=='industry':
		newName='行业新闻'
	else:
		newName='通知公告'

	newList=MyNew.objects.all().filter(
		newType=newName
		).order_by('-publishDate')
	for mynew in newList:
		html=pq(mynew.description)
		mynew.mytxt=pq(html)('p').text()
	p=Paginator(newList,5)
	if p.num_pages<=1:
		pageData=''
	else:
		page=int(request.GET.get('page',1))
		newList=p.page(page)
		left=[]
		right=[]
		left_has_more=False
		right_has_more=False
		first=False
		last=False
		total_pages=p.num_pages
		page_range=p.page_range
		if page==1:
			right=page_range[page:page+2]
			print(total_pages)
			if right[-1]<total_pages-1:
				right_has_more=True
			if right_has_more<total_pages:
				last=True
		elif page==total_pages:
			left=page_range[(page-3) if (page-3)>0 else 0:page-1]
			if left[0]>2:
				left_has_more=True
			if left[0]>1:
				first=True
		else:
			left=page_range[(page-3) if (page-3)>0 else 0:page-1]
			right=page_range[page:page+2]
			if right[-1]<total_pages-1:
				right_has_more=True
			if right_has_more<total_pages:
				last=True
			if left[0]>2:
				left_has_more=True
			if left[0]>1:
				first=True
	pageData={
			'left':left,
			'right':right,
			'left_has_more':left_has_more,
			'right_has_more':right_has_more,
			'last':last,
			'first':first,
			'total_pages':total_pages,
			'page':page,
	}	
	return render(request,'newList.html',
		{'active_menu':'news',
		'sub_menu':submenu,
		'newName':newName,
		'newList':newList,
		'pageData':pageData,})

def newDetail(request,id):
	mynew=get_object_or_404(MyNew,id=id)
	mynew.views+=1
	mynew.save()
	return render(request,'newDetail.html',{
		'active_menu':'news',
		'mynew':mynew,
		})

def search(request):
	keyword=request.GET.get('keyword')
	newList=MyNew.objects.filter(title__icontains=keyword)
	newName="关于"+"\""+keyword+"\""+"的搜索结果"
	return render(request,'searchList.html',{
		'active_menu':'news',
		'newName':newName,
		'newList':newList,
		})