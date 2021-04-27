from django import forms
from articleApp.models import Comment

class CommentForm(forms.Form):
	content=forms.CharField(label='评论')