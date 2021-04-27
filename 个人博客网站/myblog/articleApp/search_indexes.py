from haystack import indexes
from .models import Blog_Post
class Blog_PostIndex(indexes.SearchIndex,indexes.Indexable):
	text=indexes.CharField(document=True,use_template=True)
	
	def get_model(self):
		return Blog_Post

	def index_queryset(self,using=None):	
		return self.get_model().objects.all()