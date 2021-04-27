from django.db import models

# Create your models here.
from userApp.models import MyUser
from django.utils import timezone
class Board(models.Model):
	name=models.CharField(verbose_name='留言用户',max_length=50)
	email=models.EmailField(verbose_name='邮箱地址',max_length=50)
	content=models.TextField(verbose_name='留言内容',max_length=500)
	created=models.DateTimeField(verbose_name='创建时间',default=timezone.now)
	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name='访客留言'
		verbose_name_plural='访客留言'