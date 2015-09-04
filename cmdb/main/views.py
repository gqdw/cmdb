from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Host
# Create your views here.

class Searchbox(forms.Form):
	host = forms.CharField(max_length=30)

def search( request ):
#	hosts = Host.objects.all()
	if request.method == 'POST':
		form = Searchbox(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			print cd['host']
			hosts = Host.objects.filter(hostname__contains=cd['host'] )
			#hosts = Host.objects.get(hostname__iexact = cd['host'] )
			print hosts
#			host_list = []
#			for h in hosts:
#				print h.hostname.find(cd['host'])
#				if h.hostname.find(cd['host']) != -1:
#				#if h.hostname == cd['host']:
#					host_list.append(h)
	
#			return HttpResponse('ok')
			return render( request,'search.html',{ 'form':form ,'hosts':hosts})
			#return render( request,'search.html',{ 'form':form ,'hosts':host_list})
	else:
		form = Searchbox()
	return 	render( request,'search.html',{ 'form':form })
		
def listhost( request ):
	hosts = Host.objects.all()
	return render( request, 'list.html',{ 'hosts': hosts} )
