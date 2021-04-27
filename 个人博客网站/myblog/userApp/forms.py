from django import forms
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
	username=forms.CharField(required=True,label=u'用户名',
				error_messages={'required':u'请输入用户名'},
				widget=forms.TextInput(
				attrs={
				'placeholder':u'账号',
				'row':1,
				'class':'input-text size-L'
				}
				),)

	email=forms.EmailField(required=True,label=u'邮箱',
				error_messages={'required':u'请输入邮箱'},
				widget=forms.TextInput(
				attrs={
				'placeholder':u'此邮箱用于密码找回',
				'row':1,
				'class':'input-text size-L'
				}
				),)

	password1=forms.CharField(required=True,label=u'邮箱',
				error_messages={'required':u'请输入密码'},
				widget=forms.PasswordInput(
				attrs={
				'placeholder':u'密码',
				'row':1,
				'class':'input-text size-L'
				}
				),)

	password2=forms.CharField(required=True,label=u'邮箱',
				error_messages={'required':u'请再次输入密码'},
				widget=forms.PasswordInput(
				attrs={
				'placeholder':u'确认密码',
				'row':1,
				'class':'input-text size-L'
				}
				),)
	def pwd_validate(self,p1,p2):
		return p1==p2

class CaptchaTestForm(forms.Form):
	username=forms.CharField(label='用户名')
	password=forms.CharField(label='密码',widget=forms.PasswordInput)
	captcha=CaptchaField()