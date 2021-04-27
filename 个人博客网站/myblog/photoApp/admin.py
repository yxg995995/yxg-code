from django.contrib import admin
from .models import PhotoInfo
# Register your models here.
from userApp.models import MyUser
@admin.register(PhotoInfo)
class PhotoInfoAdmin(admin.ModelAdmin):
	list_display=['id','user','title','introduce','photo']

	def get_queryset(self,request):
		qs=super().get_queryset(request)
		return qs.filter(user_id=request.user.id)

	# 新增或修改数据时，设置外键可选值
	def formfield_for_foreignkey(self,db_field,request,**kwargs):
		if db_field.name == "user":
			id=request.user.id
			kwargs['queryset']=MyUser.objects.filter(id=id)
		return super().formfield_for_foreignkey(db_field,request,**kwargs)
		