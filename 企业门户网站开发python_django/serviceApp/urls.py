from django.urls import path
from . import views

app_name='serviceApp'

urlpatterns=[
	path('download/<str:docName>/',views.download,name='download'),
	path('platForm/<str:docName>/',views.platForm,name='platForm'),
	path('search/',views.search,name='search'),
	path('facedetect/',views.facedetect,name='facedetect'),
	path('facedetectDemo/',views.facedetectDemo,name='facedetectDemo')
]