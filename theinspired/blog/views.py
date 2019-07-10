from django.shortcuts import render, redirect
from .forms import FormName
from .models import QuestList
from django.views.decorators.http import require_POST



# def index(request):
# 	context = {}
# 	return render(request, 'index.html', context)

def home(request):
	context = {}
	return render(request, 'blog/home.html', context)	


def about(request):
	context={}
	return render(request, 'blog/about.html', context)


def contacts(request):
	context={}
	return render(request, 'blog/contacts.html', context)



# The functions for the wedding.html

def wedding(request):
	list=QuestList.objects.all()
	formlist=FormName()
	context={'list':list,'formlist':formlist}
	return render(request,'blog/wedding.html',context)

@require_POST
def getinvite(request):
	formlist = FormName(request.POST)
	# when creating a form first use print
	# to test if the form is working
	# print(request.POST['name'])
	# return redirect('wedding')

	if formlist.is_valid():
		new_guest = QuestList(name=request.POST['name'])
		new_guest.save()

	return redirect('wedding')	

