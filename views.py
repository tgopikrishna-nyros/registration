from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Userdetail

def index(request):
	return render(request, 'index.html')
	
def users(request):
	latest_list = Userdetail.objects.order_by('id')
	template = loader.get_template('users.html')
	context = {
		'latest_list': latest_list,
	}
	return HttpResponse(template.render(context, request))
	
def addnew(request):
	if(request.method == 'POST'):
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		contact = request.POST['contact']
		pwd = request.POST['pwd']
		cpwd = request.POST['cpwd']
		
		compose_query = Userdetail(fname=fname, lname=lname, email=email, contact=contact, password=pwd, cpassword=cpwd)
		compose_query.save()
		
		messages.add_message(request, messages.INFO, 'User registered successfully')
		
		return redirect('/registration')
	else:
		return render(request, 'addnew.html')
		
def deleteuser(request, id):
	user = Userdetail.objects.get(id=id)
	context = {
		'user':user
	}
	return render(request, 'deleteuser.html', context)
	
def deleted_user(request):
	if(request.method == 'POST'):
		remove_id = request.POST['id']
		#print(remove_id)
		
		Userdetail.objects.filter(id=remove_id).delete()
	
		return redirect('/registration')
		
def edituser(request, id):
	user = Userdetail.objects.get(id=id)
	context = {
		'user':user
	}
	return render(request, 'edituser.html', context)
	
def doedit(request):
	if(request.method == 'POST'):
		eid = request.POST['id']
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		contact = request.POST['contact']
		password = request.POST['pwd']
		cpassword = request.POST['cpwd']

		obj = Userdetail.objects.get(id=eid)
		obj.fname = fname
		obj.lname = lname
		obj.email = email
		obj.contact = contact
		obj.password = password
		obj.cpassword = cpassword
		obj.save()
		
		messages.add_message(request, messages.INFO, 'User edit success')

		return redirect('/registration')
