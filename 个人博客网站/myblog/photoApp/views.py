from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from .models import PhotoInfo
# Create your views here.
def album(request,id,page):
	albumList=PhotoInfo.objects.filter(user_id=id).order_by('id')
	paginator=Paginator(albumList,8)
	try:
		pageInfo=paginator.page(page)
	except PageNotAnInteger:
		#如果参数page的数据类型不是一个整数,就返回第一页
		pageInfo=paginator.page(1)
	except EmptyPage:
		#如果用户访问的页数大于实际页数，则返回最后一页数据
		pageInfo=paginator.page(paginator.num_pages)
	return render(request,'photo.html',locals())
