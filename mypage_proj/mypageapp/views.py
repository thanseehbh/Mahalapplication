from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from mypageapp.models import *
from mypageapp.forms import *

#Loginpage
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def index(request):
    return render(request,'mypageapp/index.html')


def register(request):

    register_status = False
    if request.method == "POST":
        # user_form = UserForm(data = request.POST)
        # user_prof_form = UserProfDet(data = request.POST)
        ##############################modified for document##########################
        user_form = UserForm(request.POST)
        user_prof_form = UserProfDet(request.POST,request.FILES)

        if user_form.is_valid() and user_prof_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = user_prof_form.save(commit=False)
            profile.user = user
            profile.save()
            register_status = True
        else:
            print(user_form.errors,user_prof_form.errors)

    else:
        user_form = UserForm()
        user_prof_form = UserProfDet()

    page_cntent = {'user_form':user_form,'user_prof_form':user_prof_form,'register_status':register_status}
    return render(request,'mypageapp/register.html',context=page_cntent)
#############################################################################################################################

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'mypageapp/login.html', {})

def mahal_page(request):
    return render(request,'mahal/layout.html')
def mahal_reg(request):
    return render(request,'mahal/appregister.html')
def user_profile_reg(request):
    return render(request,'mahal/Person_Info.html')
