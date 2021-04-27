from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
	user_id=models.AutoField(primary_key=True)
	name=models.CharField('姓名',max_length=20,default='孤独的求学者')
	introduce=models.TextField('简介',default='暂无简介')
	gender=(('male','男'),('female','女'),)
	sex=models.CharField(max_length=10,choices=gender,default='男')
	email=models.EmailField('邮箱',max_length=50,default='用户不选择公开邮箱')
	photo=models.ImageField('头像',blank=True,upload_to='images/user/')
	introduce_detail=models.TextField('自我介绍',default='暂无自我介绍')
	def __str__(self):
		return self.name
		