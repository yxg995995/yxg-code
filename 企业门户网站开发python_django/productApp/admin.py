from django.contrib import admin
from .models import Product,ProductImg
# Register your models here.
class ProductImgInline(admin.StackedInline):
	model=ProductImg
	extra=1

class ProductAdmin(admin.ModelAdmin):
	inlines=[ProductImgInline,]

admin.site.register(Product,ProductAdmin)
