from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
	context = {}
	return render(request, 'tuisd/index.html', context)

def showCaptcha(request):
	context = {}
	return render(request, 'tuisd/showCaptcha.html', context)


def showCaptchaCode(request):

	context = {

	}
	image = '18892.png'
	return render(request, 'tuisd/generatedCode.html', context, image)

def demoCaptcha(request):
	return render(request, 'tuisd/captcha/demo.html')
