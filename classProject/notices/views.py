from django.shortcuts import render

from . models import Category,Notice

from django.contrib import messages
from .form import MsgForm

categories = Category.objects.all()
data = {'categories':categories}
#or we can define categories in all the method

# Create your views here.
def home(request):
	#logic for view
	notice_list = Notice.objects.filter(isPublished=True).order_by('publishedDate').order_by('-id')[:6]
	#data = {'notice_list' : notice_list,'categories': categories}
	data['notice_list']= notice_list
	return render(request,'notices/home.html',data)

def notice(request,notice_id):
	#logic for view
	notice_detail = Notice.objects.get(id=notice_id)
#	data = {'notice_detail' : notice_detail,'categories': categories}
	data['notice_detail'] = notice_detail
	return render(request,'notices/notice.html',data)

def category(request,cat_id):
	#logic for view
	category = Category.objects.get(id=cat_id)
	notice_list = Notice.objects.filter(isPublished=True).order_by('publishedDate').filter(category=category).order_by('-id')
	#data = {'notice_list' : notice_list,"categories":categories,"category":category}
	data['notice_list'] = notice_list
	data['cat_name'] =category.name
	return render(request,'notices/category.html',data)

def aboutus(request):
	return render(request,'notices/aboutus.html',data)

def contactus(request):
	if request.method == "POST":
		form = MsgForm(request.POST)
		if form.is_valid():
			obj_msg = form.save(commit=False)
			obj_msg.save()
			messages.success(request,f'Your message is sent successfully!!!')
			return render(request,'notices/contactus.html',data)
		else:
			messages.error(request,f'Error in sending the message')
			data['msg_form'] = form
			return render(request,'notices/contactus.html',data)
	else:			
		form = MsgForm()
		data['msg_form']=form
		return render(request,'notices/contactus.html',data)



