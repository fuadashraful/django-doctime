from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

from users.forms import SignUpForm, UserLoginForm
from users.models import Profile

DOCTOR_TYPE = 1
PATIENT_TYPE = 2

def signup(request):
    context = {}

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user_type = request.POST.get('user_type', PATIENT_TYPE)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            Profile.objects.create(name=user.username, user_type=user_type, user=user)
            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))
            
            if user:
                auth.login(request, user)
            messages.success(request,"User Saved Successfully")
        else:
            messages.error(request,"Error In this form")
    else:
        form = SignUpForm()
        context[ 'form' ] = form
    
    return render(request, 'signup.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')

def login(request):
    context={}

    if request.method=="POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                auth.login(request,user)
                messages.success(request,"You Loggedin Successfully")
                return redirect('home')
            else:
                messages.error(request,"Please Provide Correct Data")
                return redirect('login')
        else:
            messages.error(request,"Some Error in login Form")
            return redirect('login')

    else:
        form=UserLoginForm()
        context[ 'form' ] = form
    
    return render(request,'login.html', context)

@login_required
def profile(request):
    
    return render(request, 'user_profile.html')