from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Function based view

def home(request):
	html_ = '''<!DOCTYPE html>
	<html>
	<head>
	</head>
	<body>
		<h1>Hello From Home!</h1>
		<p>This Is Testing Page</p>
	</body>
	</html>'''
	return HttpResponse(html_)
