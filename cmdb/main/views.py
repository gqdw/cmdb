from django.shortcuts import render

from django import forms
# Create your views here.

#class searchbox(forms.Form):
#	group = forms.

def search( request ):
#if request.method == 'POST':
	return 	render( request,'search.html',{})
		
