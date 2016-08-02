from django.shortcuts import render
from django.http import HttpResponse
import re, time
from mechanize import Browser

# Create your views here.
def index(request):
	
	# Create a browser object and give it some optional settings.
	browser = Browser()
	browser.set_all_readonly(False)
	browser.set_handle_robots(False)
	browser.set_handle_refresh(False)

	# Open a webpage
	response = browser.open("https://github.com/join?source=header-home")

	return HttpResponse(response)