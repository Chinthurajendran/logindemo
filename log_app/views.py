from django.shortcuts import render,redirect
from.models import page_data
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate

# Create your views here.
def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if page_data.objects.filter(username=username, email=email).exists():
            messages.info(request,'Username or Email is already exists')
        else:
            user_obj = page_data(username=username,email=email,password=password)
            user_obj.save()
            return redirect('login')
    return render(request,'log_html/signup_page.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_page(request):
    if 'username' in request.session:
        return redirect('home')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        if page_data.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            return redirect('home')
        else:
            messages.info(request,'invalid username and password')
            return render(request,'log_html/login_page.html')
        
    return render(request,'log_html/login_page.html')

def home_page(request):
    if 'username' in request.session and request.session['username']== 'admin':
        return redirect('admin_home')
    else:
        username = request.session['username']
    return render(request,'log_html/home_page.html',{'username':username})

def logout_button(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')
