from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs): # *args, **kwargs	
	# return HttpResponse("<h1>Hello World</h1>") # String of Html code
	return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
	return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
	context = {
		'my_text': 'this is about me',
		'my_number': 124,
		'my_list': [24, 56, 84, 34],
		'this_is_true': True,
		'some_html': '<h2>This is html in a string</h2>',
		'same_html': '<h2>This is the same html without tags</h2>'
	}
	return render(request, 'about.html', context)	
