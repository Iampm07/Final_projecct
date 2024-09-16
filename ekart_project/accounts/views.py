from django.shortcuts import render,redirect

from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request=user)

        else:
            messages.error(request,'invalid login credentials')
            return redirect,'accounts/login.html'
    return render(request,'Your are Logged out.')
def logout(request):
    auth.logout(request)
    messages.success(request,'Your are Logged out.')
    return redirect('login')