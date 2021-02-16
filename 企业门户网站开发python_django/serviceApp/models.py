from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class Docdown(models.Model):
	title=models.CharField(max_length=250,verbose_name='资料名称')
	url=models.URLField(blank=True,verbose_name='资料网址')
	publishDate=models.DateTimeField(max_length=20,
									default=timezone.now,
									verbose_name='发布时间',)
	def __str__(self):
		return self.title

	class Meta:
		ordering=['-publishDate']
		verbose_name='资料'
		verbose_name_plural=verbose_name