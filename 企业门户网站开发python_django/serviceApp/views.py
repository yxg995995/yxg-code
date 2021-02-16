from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Docdown
import numpy as np
import urllib
import json
import cv2
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
# Create your views here.
face_detector_path='serviceApp\\haarcascade_frontalface_default.xml'
face_detector=cv2.CascadeClassifier(face_detector_path)#生成人脸检测器


def download(request,docName):
	if docName=='download':
		docName='资料下载'
	submenu='资料下载'
	page=1
	left=[]
	right=[]
	left_has_more=False
	right_has_more=False
	first=False
	last=False
	total_pages=0
	page_range=0

	docList=Docdown.objects.all().filter(
		).order_by('-publishDate')
	p=Paginator(docList,5)
	if p.num_pages<=1:
		pageData=''
	else:
		page=int(request.GET.get('page',1))
		docList=p.page(page)
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
	return render(request,'docList.html',
		{'active_menu':'download',
		'sub_menu':submenu,
		'docList':docList,
		'docName':docName,
		'pageData':pageData,})
def platForm(request,docName):
	docName='人脸识别服务'
	return render(request,'platForm.html',
		{'active_menu':'platForm',
		'docName':docName,
		})

def search(request):
	keyword=request.GET.get('keyword')
	docName="关于"+"\'"+keyword+"\'"+"的结果"
	docList=Docdown.objects.filter(title__icontains=keyword)
	return render(request,'searchList.html',{
		'active_menu':'download',
		'docName':docName,
		'docList':docList,
		})

@csrf_exempt#用于规避跨站点请求攻击
def facedetect(request):
	result={}
	if request.method=='POST':
		if request.FILES.get("image",None) is not None: #读取图像
			img=read_image(stream=request.FILES['image'])
		else:
			result.update({
					"#faceNum":-1,
				})
			return JsonResponse(result)
		if img.shape[2]==3:
			img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#彩色图像转灰度
		values=face_detector.detectMultiScale(img,
											scaleFactor=1.1,
											minNeighbors=5,
											minSize=(30,30),
											flags=cv2.CASCADE_SCALE_IMAGE)
		#将检测得到的人脸检测关键点坐标封装
		values=[(int(a),int(b),int(a+c),int(b+d)) for (a,b,c,d) in values]
		request.update({
			"#faceNum":len(values),
			"faces":values,
			})
	return JsonResponse(result)

def read_image(stream=None):
	if stream is not None:
		data_temp=stream.read()
	img=np.asarray(bytearray(data_temp),dtype='uint8')
	img=cv2.imdecode(img,cv2.IMREAD_COLOR)
	return img

@csrf_exempt
def facedetectDemo(request):
	result={}
	if request.method=='POST':
		if request.FILES.get("image") is not None: #读取图像
			img=read_image(stream=request.FILES['image'])
		else:
			result.update({
					"#faceNum":-1,
				})
			return JsonResponse(default)
		if img.shape[2]==3:
			imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#彩色图像转灰度
		values=face_detector.detectMultiScale(imgGray,
											scaleFactor=1.1,
											minNeighbors=5,
											minSize=(30,30),
											flags=cv2.CASCADE_SCALE_IMAGE)
		#将检测得到的人脸检测关键点坐标封装
		values=[(int(a),int(b),int(a+c),int(b+d)) for (a,b,c,d) in values]
		for (w,x,y,z) in values:
			cv2.rectangle(img,(w,x),(y,z),(0,255,0),2)
		retval,buffer_img=cv2.imencode('.jpg',img)
		img64=base64.b64encode(buffer_img)
		img64=str(img64,encoding='utf-8')
		result['img64']=img64

	return JsonResponse(result)