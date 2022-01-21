from django.shortcuts import render, redirect
from customer import forms as CFORM
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib import messages

from product import models as PMODEL

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    RegisterForm = CFORM.RegisterForm()
    if request.method == 'POST':
        RegisterForm = CFORM.RegisterForm(request.POST)
        if RegisterForm.is_valid():
            customer=RegisterForm.save()
            customer_group=Group.objects.get_or_create(name='CUSTOMER')
            customer_group[0].user_set.add(customer)
            username=RegisterForm.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect('login')
    context={
        'RegisterForm': RegisterForm,
        }
    return render(request, 'customer/signup.html',context)

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def afterlogin_view(request):
	if is_customer(request.user):
		# messages.success(request, f"Successfully login for {request.user}")
		return redirect('/home')
	else:
		return HttpResponseRedirect('admn/dashboard')

def category_home_view(request):
    categories = PMODEL.Product_category.objects.all()
    context = {
        'categories':categories,
    }
    return render(request, 'home/home.html', context)
