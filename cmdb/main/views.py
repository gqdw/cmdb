from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Host
# Create your views here.

class Searchbox(forms.Form):
	host = forms.CharField(max_length=30)

def search( request ):
	if request.method == 'POST':
		form = Searchbox(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			print cd['host']
			return HttpResponse('ok')
	else:
		form = Searchbox()
	return 	render( request,'search.html',{ 'form':form })
		
def listhost( request ):
	hosts = Host.objects.all()
	return render( request, 'list.html',{ 'hosts': hosts} )
