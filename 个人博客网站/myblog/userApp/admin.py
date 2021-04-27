from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
class MyUserAdmin(UserAdmin):
	list_display=[
		'username','name','introduce','sex','email','photo','introduce_detail'
	]
admin.site.register(MyUser,MyUserAdmin)