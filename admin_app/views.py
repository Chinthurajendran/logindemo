from django.shortcuts import render,redirect
from log_app.models import page_data
from django.contrib import auth
from django.contrib import messages
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_login(request):
    if 'username' in request.session:
        return redirect('admin_home')
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None and username == 'admin':
            request.session['username']=username
            return redirect('admin_home')
        else:
            messages.info(request,'invalid username and password')
            return render(request,'admin_html/login_page.html')       
    return render(request,'admin_html/login_page.html')

def admin_create(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        if page_data.objects.filter(username=username).exists():
            messages.info(request,'Username or Email is already exists')
        elif page_data.objects.filter(email=email).exists():
            messages.info(request,'Username or Email is already exists')
        else:
            user_obj = page_data(username=username,password=password,email=email)
            user_obj.save()
            return redirect('admin_home')
    return render(request,'admin_html/create_page.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_home(request):
    if 'username' not in request.session:
        return redirect('admin_login')
    data= page_data.objects.all()
    return render(request,'admin_html/home_page.html',{'data':data})

def admin_logout_button(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('admin_login')

def admin_edit(request,id):
    data=page_data.objects.get(id=id)
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        edit=page_data.objects.get(id=id)
        edit.username=username
        edit.password=password
        edit.email=email
        edit.save()
        return redirect('admin_home')
    return render(request,'admin_html/edit_page.html',{'data':data})

def admin_delete(request,id):
    delete=page_data.objects.get(id=id)
    delete.delete()
    return redirect('admin_home')

def admin_search(request):
    if 'search' in request.GET:
        search = request.GET['search']
        if page_data.objects.filter(username__icontains=search).exists():
            data = page_data.objects.filter(username__icontains=search)
            return render(request, 'admin_html/home_page.html', {'data': data})
    return render(request, 'admin_html/home_page.html')
