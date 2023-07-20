from django.shortcuts import render, redirect 
from  .models import (IndexCarusel, IndexCaruselActive,
                      Category, Brand, Product,Contact,
                      Cart)
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def index(request):
    active_slider = IndexCaruselActive.objects.all().first()
    slider = IndexCarusel.objects.all()
    category_list = Category.objects.all()
    prod_list = Product.objects.all()
    brand_list = Brand.objects.all()
    return render(request, 'main/index.html', context={
        'active_slider' :active_slider,
        'slider':slider,
        'category_list':category_list,
        'prod_list' :prod_list,
        'brand_list':brand_list,
        'link':'index'
    
    })


def index_detail(request, id):
    active_slider = IndexCaruselActive.objects.all().first()
    slider = IndexCarusel.objects.all()
    category_list = Category.objects.all()
    prod_list = Brand.objects.filter(pk=id)
    brand_list = Brand.objects.all()
    return render(request, 'main/index_detail.html', context={
    'active_slider' :active_slider,
    'slider':slider,
    'category_list':category_list,
    'prod_list' :prod_list,
    'brand_list':brand_list

})


def contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.object.create(name=name, email=email, subject=subject, message=message) 
        return redirect('index')                 
    return render(request, 'main/contact-us.html' , context={
        'link':'contact'
     })

def cart(request):
    cart_list = Cart.objects.all()
    return render(request, 'main/cart.html', context={
        'cart_list':cart_list
    })

def add_to_cart(request):
    if request.method == 'POST':
        prod_id = request
        my_prod = Product.objects.get(pk=prod_id)
        Cart.objects.create(prod=my_prod)
        return redirect('index')

   
   
def delete_to_cart(request):
    if request.method =='POST':
        prod_id = request.POST.get('prod_id')
        my_prod = Product.objects.get(pk=prod_id)
        Cart.objects.filter(pk=prod_id).delete()
        return redirect('cart')
    

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")