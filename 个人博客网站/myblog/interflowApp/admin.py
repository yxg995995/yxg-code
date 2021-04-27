from django.contrib import admin
from .models import Board
from userApp.models import MyUser

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
	list_display=['name','email','content','created']
	#根据当前用户名设置数据访问权限
admin.site.register(Board,BoardAdmin)
		