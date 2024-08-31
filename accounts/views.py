from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{'form':UserCreationForm})
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect ('home')
            else:
                return render(request,'signup.html',{'form':UserCreationForm,
                                                    'error':'Passwords do not match'})
        except IntegrityError:
            return render(request,'signup.html',{'form':UserCreationForm,
                                                    'error':'User already exists'})
        
def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render (request,'login.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render (request,'login.html',{'form':AuthenticationForm,
                                                 'error':'Invalid Username'})
        else:
            login(request,user)
            return redirect('home')