from django.shortcuts import render
from django.http import HttpResponse
import re, time
from mechanize import Browser

# Create your views here.
def index(request):
	browser = Browser()
	response = browser.open("https://github.com/join?source=header-home")
	return HttpResponse(response)