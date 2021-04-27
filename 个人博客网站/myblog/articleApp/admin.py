from django.contrib import admin
from .models import *
admin.site.site_title='博客管理后台'
admin.site.site_header='博客管理'
# Register your models here.

class Blog_PostAdmin(admin.ModelAdmin):
	style_fields={'description':'ueditor'}
admin.site.register(Blog_Post,Blog_PostAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display=['article','commentator','content','created']
	#根据当前用户名设置数据访问权限
admin.site.register(Comment,CommentAdmin)