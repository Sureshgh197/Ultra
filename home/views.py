from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . models import AppUsers,UserManager,UImages
from . forms import ImageUploadForm,LoginForm
from django.contrib.auth import login,authenticate
#from home.backends import MyBackend
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model

# Create your views here.

def index(request):
    slides=UImages.objects.all()
    return render(request,"index.html",{'slides':slides})

###############################################################
###############################################################

def upload_Image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('/success')
    else:
        form = ImageUploadForm()
    return render(request, 'img.html', {'form' : form})

##############################################################
##############################################################

def accounts_register(request):
     return render(request, "register.html") 

##############################################################
##############################################################

def register(request):

    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        uname=request.POST['uname']
        email=request.POST['email']
        pwd=request.POST['pwd']
        pp=request.FILES.get('pp')
        phone=request.POST['phone']
        DOB=request.POST['dob']
        

        user=AppUsers.objects.create_user(email=email,
            profile_picture=pp,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            username=uname,
            DOB=DOB,
            password=pwd,
            )
        
        return redirect('/success')

    else:
        return render(request,'Error-Page.html')

        

##############################################################
##############################################################

def custom_login(request):
    
    # if request is not post, initialize an empty form
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
       
        if form.is_valid():
            email=request.POST.get('email')
            password = request.POST.get('password')
       
        user=authenticate(email=email,password=password)
                
        if user is not None:
            auth.login(request,user)
            obj=AppUsers.objects.get(email=email)
            #uname=obj[0]['username']
           
            uname=obj.username
            # obj2=AppUsers.objects.get(username)
            # print(obj2)
            print('user name is',obj.username)
            return redirect('/'+uname)
        else:
            return render(request, 'Error-Page.html')
    return render(request,'login.html',{'form':form}) 

#############################################################
#############################################################

def logout(request):
    auth.logout(request)
    return redirect('/')

##############################################################
##############################################################

#@login_required(login_url='/login/')
def profile(request,uname):
   
    obj=AppUsers.objects.get(username=uname)
    
    return render(request,'userpage.html',{'obj':obj})

#################################################################
#################################################################

def success(request):
    return HttpResponse('<div><h3>Account created SuccessFully</h3></div><div><button><a href="http://127.0.0.1:8000/login">Click here to Login</a></button></div>')

