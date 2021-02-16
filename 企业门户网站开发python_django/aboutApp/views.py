from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from .models import Award
def survey(request):
	return render(request,'survey.html',{'active_menu':'about','sub_menu':'survey',})

def honor(request):
	awards=Award.objects.all()
	print(awards)
	return render(request,'honor.html',
		{'active_menu':'about',
		'sub_menu':'honor',
		'awards':awards,})
	