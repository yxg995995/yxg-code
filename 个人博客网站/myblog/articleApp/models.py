from django.db import models

# Create your models here.
#模型ArticleTag设有外键字段关联模型MyUser,与模型MyUser组成一对多的数据关系
#模型ArticleInfo不仅与模型MyUser组成一对多的数据关系，并且与模型ArticleTag组成多对多的数据关系
#模型Comment只对模型ArticleInfo组成一对多的关系
from DjangoUeditor.models import UEditorField
from django.utils import timezone
from userApp.models import MyUser
class Blog_Post(models.Model):
	blog_choices=(
			('python基础','python基础'),
			('python-GUI','python-GUI'),
			('django-web','django-web'),
			('Java基础','Java基础'),
			('Java-GUI','Java-GUI'),
			('其他','其他'),
		)
	photo=models.ImageField(upload_to='Article/',blank=True)
	title=models.CharField(verbose_name='博文标题',max_length=50)
	description=UEditorField(u'内容',default='',
				width=850,height=500,
				imagePath='news/images/',
				filePath='news/files/',)
	tag=models.CharField(max_length=50,choices=blog_choices,verbose_name='博客类型')
	publishDate=models.DateTimeField(max_length=20,default=timezone.now,verbose_name='发布时间')
	views=models.PositiveIntegerField('浏览量',default=0)

	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name='博文'
		verbose_name_plural='博文'

class Comment(models.Model):
	article=models.ForeignKey(Blog_Post,on_delete=models.CASCADE,verbose_name='所属文章')
	commentator=models.CharField(max_length=50,verbose_name='匿名用户')
	content=models.TextField(verbose_name='评论内容',max_length=500)
	created=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

	def __str__(self):
		return self.content[:10]

	class Meta:
		verbose_name='评论管理'
		verbose_name_plural='评论管理'

