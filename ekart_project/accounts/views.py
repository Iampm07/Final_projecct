from django.shortcuts import render,redirect

from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required


def register(request):
    if request.methpd=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            username=email.split('@')[0]
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username)
            user.phone_number=phone_number
            user.save()
            messages.success(request,'Registrartion Successful')
            return redirect('register')
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